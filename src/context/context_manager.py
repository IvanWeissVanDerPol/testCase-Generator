import os
import json
import logging
from api.api_caller import OpenAIApiClient
from utils.utilsFile import load_config, load_context_files

config = load_config()
CONVERSATION_HISTORY_FILE = config['PATHS'].get('CONVERSATION_HISTORY_FILE', 'conversation_history.json')


def load_conversation_history() -> list:
    """Load the conversation history from a JSON file."""
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
    """Save the conversation history to a JSON file."""
    try:
        with open(CONVERSATION_HISTORY_FILE, "w", encoding="utf-8") as file:
            json.dump(conversation, file, ensure_ascii=False, indent=4)
            logging.info("Successfully saved conversation history.")
    except Exception as e:
        logging.error(f"Error saving conversation history: {e}")


def start_new_conversation() -> None:
    """Start a new conversation with the context from general_qa_docs."""
    # Load the context from the general_qa_docs folder
    context = load_context_files(config['PATHS']['PROJECT_DATA_FOLDER'])
    
    # Start the conversation with this context
    conversation = [{'role': 'system', 'content': context}]
    save_conversation_history(conversation)
    logging.info("New conversation started with general QA docs context.")



def continue_conversation(new_prompt: str) -> str:
    """Continue an existing conversation with a new prompt."""
    conversation = load_conversation_history()

    # Append the user's new prompt to the conversation
    conversation.append({'role': 'user', 'content': new_prompt})

    # Send the entire conversation to the API
    client = OpenAIApiClient()
    response = client.send_prompt("", conversation)  # Pass the conversation without an initial prompt

    if response:
        # Append the AI response to the conversation
        conversation.append({'role': 'assistant', 'content': response})
        save_conversation_history(conversation)
        return response
    else:
        logging.error("Failed to get response from OpenAI.")
        return ""
