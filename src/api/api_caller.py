import json
import requests
import logging
import os
from dotenv import load_dotenv
from utils.utilsFile import load_config, load_context_files
from utils.retry_utils import retry_with_backoff

# Load environment variables from the .env file
load_dotenv()

class OpenAIApiClient:
    def __init__(self):
        # Load the entire configuration once
        self.config = load_config()

        # Load API-related values from environment variables
        self.api_key = os.getenv('API_KEY')
        self.base_url = os.getenv('BASE_URL')

        # Load other configurations from the config file
        api_config = self.config.get('API', {})
        self.max_tokens = api_config.get('MAX_TOKENS', 1500)
        self.model = api_config.get('MODEL', 'gpt-3.5-turbo')
        self.retry_count = api_config.get('RETRY_COUNT', 3)
        self.timeout = api_config.get('TIMEOUT', 30)

        # Ensure API key and base URL are present
        if not self.api_key or not self.base_url:
            raise ValueError("API_KEY and BASE_URL must be set in the .env file.")
        
        logging.info("OpenAIApiClient initialized with API configurations.")

    def send_prompt(self, prompt: str, context_folder: str = None) -> str:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        # Load context files if folder is specified
        if context_folder:
            context_content = load_context_files(context_folder)
            prompt = f"{context_content}\n\n---\n\n{prompt}"

        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": self.max_tokens
        }

        # Send the request using retry with exponential backoff
        def send_request():
            logging.info("Sending request to OpenAI API.")
            response = requests.post(self.base_url, headers=headers, json=data, timeout=self.timeout)

            if response.status_code == 200:
                logging.info("Received response from OpenAI API.")
                return response.json().get('choices', [{}])[0].get('message', {}).get('content', '')
            else:
                logging.error(f"API call failed with status code {response.status_code}. Response: {response.text}")
                # Raise an exception to trigger retry logic
                raise Exception(f"API call failed with status code {response.status_code}")

        try:
            # Use the retry_with_backoff function for retry logic
            return retry_with_backoff(send_request, max_retries=self.retry_count)
        except Exception as e:
            logging.error(f"Error sending prompt to OpenAI API: {e}")
            return ""
