from pathlib import Path
import streamlit as st
from modules.openai_service import OpenAIService

class AgentProcessor:
    def __init__(self, config_loader, selected_language: str, vendor: str, artifacts_dir: Path):
        self.config_loader = config_loader
        self.selected_language = selected_language
        self.vendor = vendor
        self.artifacts_dir = artifacts_dir
        self.log_file_path = self.artifacts_dir / "agent.log"

        # Carrega a configuração dos agentes para este idioma e fornecedor
        self.agents_config = self.config_loader.get("languages")[self.selected_language]["agents"].get(vendor, {})

    def _log_message(self, message: str):
        """
        Escreve uma mensagem de log tanto no arquivo .log quanto no Streamlit.
        """
        with self.log_file_path.open("a", encoding="utf-8") as log_file:
            log_file.write(message + "\n")
        st.write(message)

    def process_files(self, markdown_files: list) -> str:
        """
        Orquestra o processamento de uma lista de arquivos Markdown
        através de uma cadeia de agentes (Requisitor, ControlGen, etc.).
        Retorna o resultado final do último agente.
        """
        st.subheader("🚀 Starting baseline creation")

        self._log_message("📌 **[STEP 1/5] Extracting requirements**")
        for md_file in markdown_files:
            original_text = self._read_file_content(md_file)
            self.run_agent("Requisitor", original_text, md_file)

        self._log_message("📌 **[STEP 2/5] Transforming requirements into automatable controls**")
        controlgen_outputs = []
        for md_file in markdown_files:
            requisitor_file = self.artifacts_dir / f"{md_file.stem}_Requisitor.md"
            requisitor_output = self._read_file_content(requisitor_file)

            gen_out = self.run_agent("ControlGen", requisitor_output, md_file)
            controlgen_outputs.append(gen_out)

        self._log_message("📌 **[STEP 3/5] Unifying controls**")
        unified_controlgen = "\n\n".join(
            f"### ControlGen Output - File {idx+1}\n{text}"
            for idx, text in enumerate(controlgen_outputs)
        )
        controlgen_merged_file = self.artifacts_dir / "controlgen_unified.md"
        controlgen_merged_file.write_text(unified_controlgen, encoding="utf-8")

        self._log_message("📌 **[STEP 4/5] Refining Controls**")
        refiner_out = self.run_agent("ControlRefiner", unified_controlgen, controlgen_merged_file)

        self._log_message("📌 **[STEP 5/5] Evaluating Risks**")
        final_out = self.run_agent("RiskEvaluator", refiner_out, controlgen_merged_file)

        return final_out

    def run_agent(self, agent_name: str, content: str, md_file: Path) -> str:
        """
        Executa um agente de IA específico, registra tokens, custo
        e salva o output retornado em um arquivo .md.
        """
        agent_info = self.agents_config.get(agent_name)
        if not agent_info:
            self._log_message(f"⚠️ [WARNING] Agent `{agent_name}` not configured. Skipping.")
            return content

        agent_id = agent_info.get("identifier", "")
        if not agent_id or "PLACEHOLDER" in agent_id:
            self._log_message(f"⚠️ [WARNING] Agent `{agent_name}` has no valid identifier. Skipping.")
            return content

        prompt = f"Function: {agent_info['function']}\n\nContent:\n{content}"
        prompt_tokens = OpenAIService.count_tokens(prompt, model="gpt-4o")

        processed_content = "\n".join(
            OpenAIService.run_assistant(prompt, agent_id)
        )
        completion_tokens = OpenAIService.count_tokens(processed_content, model="gpt-4o")

        # Calcula custo para este agente
        token_info = OpenAIService.calculate_cost(prompt_tokens, completion_tokens, model="gpt-4o")

        # Armazena os custos em session_state para somar ao final
        if "agent_costs" not in st.session_state:
            st.session_state["agent_costs"] = {}

        if agent_name not in st.session_state["agent_costs"]:
            st.session_state["agent_costs"][agent_name] = {
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_cost": 0.0
            }

        st.session_state["agent_costs"][agent_name]["prompt_tokens"] += token_info["prompt_tokens"]
        st.session_state["agent_costs"][agent_name]["completion_tokens"] += token_info["completion_tokens"]
        st.session_state["agent_costs"][agent_name]["total_cost"] += token_info["total_cost"]



        # Exibe detalhes em um "expander" no Streamlit
        #with st.expander("Tokens used and Cost"):
        #    st.write(f"**Agent:** {agent_name}")
        #    st.write(f"**Tokens Sent:** {token_info['prompt_tokens']}")
        #    st.write(f"**Tokens Received:** {token_info['completion_tokens']}")
        #    st.write(f"**Total Cost:** US$ {token_info['total_cost']:.4f}")

        # Salva o conteúdo gerado em um arquivo .md
        output_path = self.artifacts_dir / f"{md_file.stem}_{agent_name}.md"
        output_path.write_text(processed_content, encoding="utf-8")

        return processed_content

    def _read_file_content(self, md_file: Path) -> str:
        """
        Lê o conteúdo de um arquivo Markdown.
        Retorna string vazia se o arquivo não existir.
        """
        if not md_file.exists():
            return ""
        return md_file.read_text(encoding="utf-8")
