from pathlib import Path
import streamlit as st
from modules.openai_service import OpenAIService

class AgentProcessor:
    """
    Responsável por gerenciar o processamento sequencial dos agentes.
    """

    def __init__(self, config_loader, selected_language: str, artifacts_dir: Path):
        self.config_loader = config_loader
        self.selected_language = selected_language
        self.artifacts_dir = artifacts_dir

        # Ordem definida de agentes
        self.agent_order = [
            "Requisitor",
            "ControlGen",
            "RiskEvaluator",
            "Consolidator",
            "Reviewer"
        ]

        # Carrega as configurações dos agentes a partir do config.json
        self.agents_config = self.config_loader.get("languages")[self.selected_language]["agents"]

    def process_file(self, md_file: Path, id_unico: str) -> str:
        """
        Processa um arquivo Markdown através da cadeia de agentes.
        Retorna o conteúdo final processado para o arquivo.
        """
        with md_file.open("r", encoding="utf-8") as file:
            content = file.read()

        for agent in self.agent_order:
            agent_info = self.agents_config.get(agent)
            if not agent_info:
                st.warning(f"Agente '{agent}' não configurado. Pulando para o próximo.")
                continue
            
            agent_id = agent_info.get("identifier", "")
            if not agent_id or "PLACEHOLDER" in agent_id:
                st.info(f"Agente '{agent}' não implementado (placeholder). Pulando para o próximo.")
                continue

            # Constrói o prompt com base na função do agente e conteúdo atual
            prompt = f"ID: {id_unico}\nFunção: {agent_info['function']}\n\nConteúdo:\n{content}"
            output_file = self.artifacts_dir / f"{md_file.stem}_{agent}.md"
            st.info(f"Processando com o agente: {agent} (ID: {agent_id})")

            # Chama a API da OpenAI com o assistente correto
            content = "\n".join(self._process_prompt(prompt, content, output_file, agent_id))

        return content

    def _process_prompt(self, prompt: str, content: str, output_file: Path, agent_id: str) -> list:
        """
        Combina o prompt com o conteúdo e chama o assistente para processar.
        Salva as respostas em um arquivo e retorna a lista de respostas.
        """
        combined_prompt = f"{prompt}\n\n{content}"
        responses = OpenAIService.run_assistant(combined_prompt, agent_id)

        with output_file.open("w", encoding="utf-8") as f:
            f.write("\n".join(responses))

        return responses

    def process_files(self, markdown_files: list, id_unico: str) -> str:
        """
        Processa uma lista de arquivos Markdown e consolida as respostas finais.
        Retorna o conteúdo consolidado.
        """
        final_content = ""
        for md_file in markdown_files:
            file_content = self.process_file(md_file, id_unico)
            final_content += file_content + "\n"
        return final_content
