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
            # List existing assistants
            assistants = client.beta.assistants.list(limit=20)
            for assistant in assistants.data:
                # Check if the assistant name matches "CyberSecurityAssistant"
                if assistant.name == "CyberSecurityAssistant":
                    return assistant.id

            # Create a new assistant
            new_assistant = client.beta.assistants.create(
                instructions=assistant_info["instructions"],
                name=assistant_info["name"],
                tools=assistant_info["tools"],
                model=assistant_info["model"]
            )
            return new_assistant.id
        except Exception as e:
            raise RuntimeError(f"Error creating or retrieving assistant: {e}")

    @staticmethod
    def initialize_assistant(config_path: str) -> str:
        """
        High-level method to initialize an assistant using the config file.

        Args:
            config_path (str): Path to the configuration file.

        Returns:
            str: Assistant ID.
        """
        # Load configuration
        config_loader = ConfigLoader(config_path)
        assistant_info = config_loader.get("assistant_info")

        if not assistant_info:
            raise ValueError("Assistant information is missing in the configuration.")

        # Initialize the client and create/retrieve the assistant
        client = OpenAIService.setup_client()  # Directly fetches the API key
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

            # Initialize the client
            client = OpenAIService.setup_client()  # Directly fetches the API key

            # Create a thread and send the message
            thread = client.beta.threads.create()
            client.beta.threads.messages.create(thread.id, role="user", content=content)

            # Run the assistant
            run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=assistant_id)

            responses = []
            while True:
                # Check the status of the run
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
