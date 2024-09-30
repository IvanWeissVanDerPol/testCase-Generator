import json
import requests
import logging
import os
from dotenv import load_dotenv
from utils.utilsFile import load_config

# Load environment variables from the .env file
load_dotenv()

class OpenAIApiClient:
    def __init__(self):
        self.config = load_config()
        self.api_key = os.getenv('API_KEY')
        self.base_url = os.getenv('BASE_URL')
        api_config = self.config.get('API', {})
        self.max_tokens = api_config.get('MAX_TOKENS', 4000)
        self.model = api_config.get('MODEL', 'gpt-4')
        self.retry_count = api_config.get('RETRY_COUNT', 3)
        self.timeout = api_config.get('TIMEOUT', 30)

        if not self.api_key or not self.base_url:
            raise ValueError("API_KEY and BASE_URL must be set in the .env file.")
        
        logging.info("OpenAIApiClient initialized with API configurations.")
    def send_prompt(self, prompt: str = "", conversation: list = None) -> str:
        """Send the entire conversation history as a prompt to the OpenAI API."""
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        # Ensure conversation history is provided and in the right format
        if not conversation:
            conversation = [{"role": "user", "content": prompt}]
        else:
            conversation = conversation  # Send the full conversation
        
        data = {
            "model": self.model,
            "messages": conversation,
            "max_tokens": self.max_tokens
        }

        try:
            logging.info("Sending conversation to OpenAI API.")
            response = requests.post(self.base_url, headers=headers, json=data)

            if response.status_code == 200:
                logging.info("Received response from OpenAI API.")
                return response.json().get('choices', [{}])[0].get('message', {}).get('content', '')
            else:
                logging.error(f"API call failed with status code {response.status_code}. Response: {response.text}")
                return ""
        except Exception as e:
            logging.error(f"Error sending prompt to OpenAI API: {e}")
            return ""


