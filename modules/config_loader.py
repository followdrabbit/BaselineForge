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
        """Retrieve a value from the configuration data."""
        return self.config_data.get(key, default)

    def get_language_config(self, language):
        """Get the configuration for the specified language."""
        return self.config_data.get("languages", {}).get(language, {})

    def get_menu(self, language):
        """Get the menu configuration for the specified language."""
        language_config = self.get_language_config(language)
        return language_config.get("ui", {}).get("menu", {})

    def get_version_info(self, language):
        """Get the version configuration for the specified language."""
        language_config = self.get_language_config(language)
        version_info = language_config.get("ui", {}).get("version_info", {})

        # Ensure required keys exist
        required_keys = ["version", "status", "draft"]
        if not all(key in version_info for key in required_keys):
            missing_keys = [key for key in required_keys if key not in version_info]
            raise ValueError(f"Missing required keys in version_info: {missing_keys}")

        return version_info

    def get_categories(self, language):
        """Get the categories for the specified language."""
        language_config = self.get_language_config(language)
        return language_config.get("categories", [])

    def get_control_table(self, language):
        """Get the control table labels for the specified language."""
        language_config = self.get_language_config(language)
        return language_config.get("ui", {}).get("control_table", {})

    def get_html_sections(self, language):
        """Get the HTML sections for the specified language."""
        language_config = self.get_language_config(language)
        return language_config.get("ui", {}).get("html_sections", {})

    def get_history_table(self, language):
        """Get the history table labels for the specified language."""
        language_config = self.get_language_config(language)
        return language_config.get("ui", {}).get("history_table", {})

    def get_prompts(self, language):
        """Get prompts for the specified language."""
        language_config = self.get_language_config(language)
        prompt_files = language_config.get("prompt_files", [])

        if len(prompt_files) != 3:
            raise ValueError(f"Invalid prompt_files configuration for language {language}: {prompt_files}")

        # Load prompt file contents
        prompts = []
        for file_path in prompt_files:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    prompts.append(file.read())
            except FileNotFoundError:
                raise FileNotFoundError(f"Prompt file not found: {file_path}")

        return prompts
