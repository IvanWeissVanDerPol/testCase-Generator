import os
import json
import logging
from utils.utilsFile import load_configuration

config = load_configuration()
CONVERSATION_HISTORY_FILE = config.get('CONVERSATION_HISTORY_FILE', 'conversation_history.json')

def load_conversation_history() -> list:
    try:
        if os.path.exists(CONVERSATION_HISTORY_FILE):
            with open(CONVERSATION_HISTORY_FILE, "r", encoding="utf-8") as file:
                conversation = json.load(file)
                logging.info("Successfully loaded conversation history.")
                return conversation
        else:
            logging.warning(f"Conversation history file not found: {CONVERSATION_HISTORY_FILE}")
            return []
    except Exception as e:
        logging.error(f"Error loading conversation history: {e}")
        return []

def save_conversation_history(conversation: list) -> None:
    try:
        with open(CONVERSATION_HISTORY_FILE, "w", encoding="utf-8") as file:
            json.dump(conversation, file, ensure_ascii=False, indent=4)
            logging.info("Successfully saved conversation history.")
    except Exception as e:
        logging.error(f"Error saving conversation history: {e}")

def save_content_to_file(file_path: str, content: str) -> None:
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
            logging.info(f"Successfully saved content to {file_path}.")
    except Exception as e:
        logging.error(f"Error saving file {file_path}: {e}")
