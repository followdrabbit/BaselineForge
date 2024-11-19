from modules.openai_service import OpenAIService

class PromptProcessor:
    def __init__(self, assistant_id):
        self.assistant_id = assistant_id

    def process_prompt(self, prompt, content, output_file):
        """
        Processa um único prompt com conteúdo fornecido e salva a resposta em um arquivo.

        Args:
            prompt (str): O prompt a ser processado.
            content (str): O conteúdo a ser combinado com o prompt.
            output_file (str): Caminho do arquivo para salvar as respostas.

        Returns:
            tuple: Uma tupla contendo o caminho do arquivo gerado e as respostas.
        """
        # Combinar o prompt e o conteúdo
        combined_prompt = f"{prompt}\n\n{content}"
        # Chamar o assistente para processar o prompt
        responses = OpenAIService.run_assistant(combined_prompt, self.assistant_id)

        # Salvar as respostas no arquivo
        with open(output_file, "w", encoding="utf-8") as file:
            file.write("\n".join(responses))

        # Retornar o caminho do arquivo e as respostas
        return output_file, responses
