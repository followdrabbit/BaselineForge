import time
from openai import OpenAI
from modules.config_loader import ConfigLoader
import streamlit as st

class OpenAIService:
    """Handles interaction with the OpenAI API."""

    @staticmethod
    def setup_client(api_key: str = None) -> OpenAI:
        """
        Initializes the OpenAI client with the provided API key or retrieves it from Streamlit secrets.

        Args:
            api_key (str): Optional OpenAI API key. If not provided, it retrieves the key from Streamlit secrets.

        Returns:
            OpenAI: Initialized OpenAI client.
        """
        if not api_key:
            api_key = st.secrets.get("OpenAI_key")
            if not api_key:
                raise ValueError("API key is required to initialize OpenAI client.")
        return OpenAI(api_key=api_key)

    @staticmethod
    def create_or_get_assistant(client, assistant_info: dict) -> str:
        """
        Creates or retrieves an assistant by name.

        Args:
            client (OpenAI): OpenAI client instance.
            assistant_info (dict): Dictionary with assistant creation parameters.

        Returns:
            str: Assistant ID.
        """
        try:
            # Lista os assistentes existentes
            assistants = client.beta.assistants.list(limit=20)
            # Verifica se já existe um assistente com o nome especificado
            for assistant in assistants.data:
                if assistant.name == assistant_info.get("name", "CyberSecurityAssistant"):
                    return assistant.id

            # Cria um novo assistente (pode ser necessário fornecer configurações adicionais)
            new_assistant = client.beta.assistants.create(
                instructions=assistant_info.get("instructions", ""),
                name=assistant_info.get("name", "CyberSecurityAssistant"),
                tools=assistant_info.get("tools", []),
                model=assistant_info.get("model", "gpt-4")
            )
            return new_assistant.id
        except Exception as e:
            raise RuntimeError(f"Error creating or retrieving assistant: {e}")

    @staticmethod
    def initialize_assistant(config_path: str, selected_language: str, vendor: str) -> str:
        """
        High-level method to initialize an assistant using the config file, selected language, and vendor.

        Args:
            config_path (str): Path to the configuration file.
            selected_language (str): Language code to select the appropriate assistant configuration.
            vendor (str): Cloud service provider (e.g., "AWS", "Azure", "GCP", "Huawei").

        Returns:
            str: Assistant ID.
        """
        # Carrega a configuração utilizando o ConfigLoader
        config_loader = ConfigLoader(config_path)
        try:
            # Acessa a seção de agentes para o idioma selecionado e o provider específico
            agents = config_loader.get("languages")[selected_language]["agents"][vendor]
        except KeyError:
            raise ValueError(f"Assistant configuration for vendor '{vendor}' is missing in the configuration for language '{selected_language}'.")

        # Selecionamos o agente "Requisitor" como padrão (ajuste se necessário)
        assistant_info = agents.get("Requisitor")
        if not assistant_info:
            raise ValueError(f"Assistant 'Requisitor' information is missing in the configuration for vendor '{vendor}' and language '{selected_language}'.")

        # Se o identificador já estiver definido, retorne-o diretamente
        if "identifier" in assistant_info and assistant_info["identifier"]:
            return assistant_info["identifier"]

        # Caso contrário, inicializa o cliente e cria/recupera o assistente
        client = OpenAIService.setup_client()  # Obtém a chave de API do Streamlit secrets
        return OpenAIService.create_or_get_assistant(client, assistant_info)

    @staticmethod
    def run_assistant(content: str, assistant_id: str):
        """
        Runs the OpenAI assistant and processes the content.

        Args:
            content (str): Content to be processed by the assistant.
            assistant_id (str): Identifier for the OpenAI assistant.

        Returns:
            List[str]: Responses from the assistant.
        """
        try:
            if not assistant_id:
                raise ValueError("Assistant ID is required to run the OpenAI assistant.")

            # Inicializa o cliente
            client = OpenAIService.setup_client()  # Obtém a chave de API do Streamlit secrets

            # Cria uma thread e envia a mensagem
            thread = client.beta.threads.create()
            client.beta.threads.messages.create(thread.id, role="user", content=content)

            # Executa o assistente
            run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=assistant_id)

            responses = []
            while True:
                # Verifica o status da execução
                run_status = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id).status
                if run_status == "completed":
                    messages = client.beta.threads.messages.list(thread_id=thread.id)
                    responses = [msg.content[0].text.value for msg in messages if msg.role == "assistant"]
                    break
                elif run_status in ["queued", "in_progress"]:
                    time.sleep(3)
                else:
                    raise RuntimeError(f"Unexpected run status: {run_status}")

            return responses
        except Exception as e:
            raise RuntimeError(f"Error during OpenAI assistant execution: {e}")
