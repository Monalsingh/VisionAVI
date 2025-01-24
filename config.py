import yaml
import os

class ConfigManager:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self):
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found at {self.config_path}")
        with open(self.config_path, 'r') as file:
            return yaml.safe_load(file)

    def get(self, key: str, default=None):
        # Get a specific configuration value
        return self.config.get(key, default)

    def get_all(self):
        # Get the entire configuration as a dictionary
        return self.config
