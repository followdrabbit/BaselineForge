
import json

class ConfigLoader:
    def __init__(self, config_file="config/config.json"):
        self.config_file = config_file
        self.config_data = self.load_config()
        
    def load_config(self):
        """Load the JSON configuration file."""
        try:
            with open(self.config_file, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The configuration file {self.config_file} was not found.")
            return {}
        except json.JSONDecodeError as e:
            print(f"Error: Failed to parse the configuration file {self.config_file}: {e}")
            return {}

    def get(self, key, default=None):
        """
        Retrieve a value from the configuration data.
        Args:
            key (str): The key to look up in the configuration.
            default: The value to return if the key is not found.

        Returns:
            The value associated with the key, or the default value if the key is not found.
        """
        return self.config_data.get(key, default)

    def get_language_config(self, language):
        """Get the configuration for the specified language."""
        return self.config_data.get("languages", {}).get(language, {})

    def get_menu(self, language):
        """Get the menu configuration for the specified language."""
        language_config = self.get_language_config(language)
        return language_config.get("menu", {})

    def get_categories(self, language):
        """Get the categories for the specified language."""
        language_config = self.get_language_config(language)
        categories = language_config.get("categories", [])
        if not isinstance(categories, list):
            print(f"Invalid categories format for language {language}: {categories}")
            return []
        return categories

    def get_control_table(self, language):
        """Get the control table labels for the specified language."""
        language_config = self.get_language_config(language)
        return language_config.get("control_table", {})

    def get_html_sections(self, language):
        """Get the HTML sections for the specified language."""
        language_config = self.get_language_config(language)
        return language_config.get("html_sections", {})

    def get_history_table(self, language):
        """Get the history table labels for the specified language."""
        language_config = self.get_language_config(language)
        return language_config.get("history_table", {})
    
    def get_prompts(self, language):
        """Get prompts for the specified language."""
        language_config = self.get_language_config(language)
        prompt_files = language_config.get("prompt_files", [])
        if len(prompt_files) != 2:
            raise ValueError(f"Invalid prompt_files configuration for language {language}: {prompt_files}")

        # Carregar o conteúdo dos arquivos de prompt
        prompts = []
        for file_path in prompt_files:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    prompts.append(file.read())
            except FileNotFoundError:
                raise FileNotFoundError(f"Prompt file not found: {file_path}")
        return prompts

