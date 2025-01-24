import os
from core.util.utils import dummy_print
from config import ConfigManager

def main():
    # Define the path to the central_config.yaml file
    config_path = "config.yaml"

    # Load the configuration using ConfigManager
    config_manager = ConfigManager(config_path)
    app_config = config_manager.get_all()

    # Access specific configurations
    # Using get() method with key and value
    project_name = config_manager.get("app")["name"]
    project_version = config_manager.get("app")["version"]
    batch_name = config_manager.get("app")["batch"]

    if app_config['logging']['enable']:
        if app_config['logging']['level'] == 'level-1':
            dummy_print(project_name, project_version, batch_name)
            
    # Using get() method with only key
    dummy_config = config_manager.get("dummy")

    if dummy_config['task'] == 'add':
        print(f"Addition answer is : {dummy_config['variable_1'] + dummy_config['variable_2']}")
    else:
        print("Please specify task in config or implement task mentioned in config.")

if __name__ == "__main__":
    main()
