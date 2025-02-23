from pathlib import Path
import streamlit as st
from modules.openai_service import OpenAIService

class AgentProcessor:
    """
    Handles sequential processing of Markdown files through multiple AI assistants.

    Fluxo sugerido:
      1) Requisitor -> roda em cada arquivo separadamente
      2) ControlGen -> roda em cada arquivo (lendo a saída do Requisitor)
      3) Unifica todos os resultados de ControlGen
      4) ControlRefiner -> roda uma única vez no texto unificado de ControlGen
      5) RiskEvaluator -> roda uma única vez no resultado do ControlRefiner

    Observação:
     - Removidos os passos 6) ControlMerger e 7) Reviewer.
     - Não usamos session_id e run_id aqui. Se quiser, crie os diretórios no `main.py`.
     - Os nomes dos arquivos .md gerados são baseados apenas em "<md_file.stem>_<agent_name>.md".
     - Os logs são gravados em "agent.log" dentro de `artifacts_dir`.
    """

    def __init__(self, config_loader, selected_language: str, artifacts_dir: Path):
        self.config_loader = config_loader
        self.selected_language = selected_language
        self.artifacts_dir = artifacts_dir

        # Arquivo fixo de log no diretório de artefatos
        self.log_file_path = self.artifacts_dir / "agent.log"

        # Carrega as configs dos agentes a partir do config.json
        self.agents_config = self.config_loader.get("languages")[self.selected_language]["agents"]

    def _log_message(self, message: str):
        """
        Escreve uma mensagem de log (prompt, resposta ou informativo) no arquivo de log.
        """
        with self.log_file_path.open("a", encoding="utf-8") as log_file:
            log_file.write(message + "\n")

    def process_files(self, markdown_files: list) -> str:
        """
        Executa o fluxo:
          1) Requisitor por arquivo
          2) ControlGen por arquivo
          3) Unifica resultados de ControlGen
          4) ControlRefiner no texto unificado
          5) RiskEvaluator no resultado do ControlRefiner

        Retorna o texto final após o RiskEvaluator.
        """

        # -----------------------------
        # 1) Requisitor em cada arquivo
        # -----------------------------
        self._log_message("==[ETAPA 1] Requisitor por arquivo==")
        for md_file in markdown_files:
            original_text = self._read_file_content(md_file)
            self.run_agent("Requisitor", original_text, md_file)

        # -----------------------------
        # 2) ControlGen em cada arquivo
        # -----------------------------
        self._log_message("==[ETAPA 2] ControlGen por arquivo==")
        controlgen_outputs = []
        for md_file in markdown_files:
            requisitor_file = self.artifacts_dir / f"{md_file.stem}_Requisitor.md"
            requisitor_output = self._read_file_content(requisitor_file)

            gen_out = self.run_agent("ControlGen", requisitor_output, md_file)
            controlgen_outputs.append(gen_out)

        # -----------------------------
        # 3) Unificar resultados do ControlGen
        # -----------------------------
        self._log_message("==[ETAPA 3] Unificando ControlGen==")
        unified_controlgen = "\n\n".join(
            f"### ControlGen Output - Arquivo {idx+1}\n{text}"
            for idx, text in enumerate(controlgen_outputs)
        )
        controlgen_merged_file = self.artifacts_dir / "controlgen_unificado.md"
        controlgen_merged_file.write_text(unified_controlgen, encoding="utf-8")

        # -----------------------------
        # 4) ControlRefiner
        # -----------------------------
        self._log_message("==[ETAPA 4] ControlRefiner==")
        refiner_out = self.run_agent("ControlRefiner", unified_controlgen, controlgen_merged_file)

        # -----------------------------
        # 5) RiskEvaluator
        # -----------------------------
        self._log_message("==[ETAPA 5] RiskEvaluator==")
        final_out = self.run_agent("RiskEvaluator", refiner_out, controlgen_merged_file)

        self._log_message("==[FLUXO FINALIZADO]==")
        return final_out

    def run_agent(self, agent_name: str, content: str, md_file: Path) -> str:
        """
        Executa um agente. Gera:
           <md_file.stem>_<agent_name>.md

        Exemplo: se md_file = "controlgen_unificado.md", e agent_name = "ControlRefiner",
          -> "controlgen_unificado_ControlRefiner.md"
        """
        agent_info = self.agents_config.get(agent_name)
        if not agent_info:
            self._log_message(f"[AVISO] Agente '{agent_name}' não configurado. Pulando.")
            return content

        agent_id = agent_info.get("identifier", "")
        if not agent_id or "PLACEHOLDER" in agent_id:
            self._log_message(f"[AVISO] Agente '{agent_name}' sem identifier válido. Pulando.")
            return content

        prompt = (
            f"Function: {agent_info['function']}\n\n"
            f"Content:\n{content}"
        )

        # Loga o prompt
        self._log_message(f"\n--- [AGENTE: {agent_name}] PROMPT ---\n{prompt}\n---")

        # Chama OpenAI
        processed_content = "\n".join(OpenAIService.run_assistant(prompt, agent_id))

        # Loga a resposta
        self._log_message(f"--- [AGENTE: {agent_name}] RESPONSE ---\n{processed_content}\n--- END ---\n")

        # Salva <md_file.stem>_<agent_name>.md
        output_path = self.artifacts_dir / f"{md_file.stem}_{agent_name}.md"
        output_path.write_text(processed_content, encoding="utf-8")

        return processed_content

    def _read_file_content(self, md_file: Path) -> str:
        if not md_file.exists():
            return ""
        return md_file.read_text(encoding="utf-8")
