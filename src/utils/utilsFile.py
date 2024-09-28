import json
import logging
import os

def load_config(config_path="config\\config.json") -> dict:
    """
    Loads the configuration from the specified config.json file.

    Parameters:
        config_path (str): Path to the config.json file.

    Returns:
        dict: The loaded configuration as a dictionary.
    """
    try:
        logging.info(f"Loading configuration from: {config_path}")
        with open(config_path, "r", encoding="utf-8") as config_file:
            config = json.load(config_file)
            logging.info(f"Configuration loaded successfully from {config_path}")
            return config
    except FileNotFoundError:
        logging.error(f"Configuration file not found: {config_path}")
        return {}
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding config file: {e}")
        return {}

def save_content_to_file(file_path: str, content: str) -> None:
    """
    Saves the provided content to the specified file path.

    Parameters:
        file_path (str): The path to the file.
        content (str): The content to be saved.
    """
    try:
        logging.info(f"Saving content to file: {file_path}")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
            logging.info(f"Successfully saved content to {file_path}")
    except Exception as e:
        logging.error(f"Error saving file {file_path}: {e}")

def load_template(template_path: str) -> str:
    """
    Loads the template from the specified path.

    Parameters:
        template_path (str): The path to the template file.

    Returns:
        str: The content of the template file.
    """
    try:
        logging.info(f"Loading template from: {template_path}")
        with open(template_path, "r", encoding="utf-8") as template_file:
            template = template_file.read()
            logging.info(f"Successfully loaded template from {template_path}")
            return template
    except FileNotFoundError:
        logging.error(f"Template file not found: {template_path}")
        return ""
    except Exception as e:
        logging.error(f"Error loading template file: {e}")
        return ""

def load_context_files(context_folder: str) -> str:
    """
    Loads all files from the specified context folder and concatenates their content into a single string.
    """
    context_content = ""
    for root, _, files in os.walk(context_folder):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    context_content += f"\n\n---\n\n{f.read()}"
                    logging.info(f"Loaded context file: {file_path}")
            except Exception as e:
                logging.error(f"Error loading file {file_path}: {e}")
    return context_content
