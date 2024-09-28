import json
import logging
import os
import re
import time
import sys

# Set up project root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)


from utils.directory_utils import ensure_directory_exists
from utils.prompt_renderer import render_prompt

# Set up project root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from api.api_caller import OpenAIApiClient
from documentation.document_generator import create_test_suite, create_test_cases
from utils.utilsFile import load_context_files, load_config

# Load configuration
config = load_config("config\\config.json")

logging.basicConfig(
    filename='suite_case_generation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def extract_test_cases_from_suite(suite_description: str) -> list:
    client = OpenAIApiClient()
    variables = {
        'suite_description': suite_description
    }
    full_prompt = render_prompt('extract_test_cases.md', variables)

    logging.info("Extracting test cases from suite description using OpenAI.")

    try:
        response = client.send_prompt(full_prompt)
        cleaned_response = re.sub(r'```json|```', '', response).strip()
        test_cases = json.loads(cleaned_response)
        logging.info(f"Extracted test cases: {test_cases}")
        return test_cases
    except Exception as e:
        logging.error(f"Error extracting test cases: {e}")
        return []


def generate_test_cases_from_suite( suite_path: str = None):
    # time.sleep(config.get('GENERAL').get('SLEEP_TIME'))
    # context_folder = config.get('PATHS').get('PROJECT_DATA_FOLDER')
    # context = load_context_files(context_folder)
    
    if suite_path:
        if os.path.exists(suite_path):
            logging.info(f"Generating test cases based on suite file at {suite_path}")
            with open(suite_path, "r", encoding="utf-8") as suite_file:
                suite_description = suite_file.read()

            suite_id = os.path.basename(suite_path).split(".")[0]
            test_cases = extract_test_cases_from_suite(suite_description)

            # Ensure the test case directory exists
            output_dir = f"{config['PATHS']['TEST_CASE_PATH']}/{suite_id}"
            ensure_directory_exists(output_dir)
            create_test_cases(suite_id, suite_description, test_cases)
        else:
            logging.error(f"Test suite file not found at {suite_path}")
    else:
        logging.warning("No suite path provided.")

if __name__ == "__main__":
    print(os.getcwd())  # Prints current working directory
    generate_test_cases_from_suite(suite_path="resulting_docs\\test_suites\\Functional_Test_Suite\\Functional Test Suite - Mobile App.md")
