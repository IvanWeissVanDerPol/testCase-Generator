import logging
import os
from api.api_caller import OpenAIApiClient
from utils.utilsFile import load_template, save_content_to_file, load_config
from utils.prompt_renderer import render_prompt
from utils.directory_utils import ensure_directory_exists

# Load the configuration from the JSON file
config = load_config()

# Load templates and configuration values from the JSON file
TEMPLATE_TEST_CASE = load_template(config['TEMPLATES']['TEST_CASE_TEMPLATE'])
TEMPLATE_TEST_SUITE = load_template(config['TEMPLATES']['TEST_SUITE_TEMPLATE'])
PROMPT_DETAILED_TEST_CASE = config['PROMPTS']['DETAILED_TEST_CASE_GENERATION']
PROMPT_TEST_SUITE_GENERATION = config['PROMPTS']['TEST_SUITE_GENERATION']
TEST_SUITE_PATH = config['PATHS']['TEST_SUITE_PATH']
TEST_CASE_PATH = config['PATHS']['TEST_CASE_PATH']

def create_test_suite(prompt: str) -> str:
    client = OpenAIApiClient()
    variables = {
        'template': TEMPLATE_TEST_SUITE,
        'description': prompt
    }
    full_prompt = render_prompt(PROMPT_TEST_SUITE_GENERATION, variables)

    logging.info(f"Creating test suite with prompt: {prompt}")

    try:
        response = client.send_prompt(full_prompt)
        if response:
            file_path = os.path.join(TEST_SUITE_PATH, 'generated_test_suite.txt')
            ensure_directory_exists(os.path.dirname(file_path))
            save_content_to_file(file_path, response)
            logging.info(f"Test suite saved to {file_path}")
            return file_path
        else:
            logging.error("Failed to generate test suite.")
            return ""
    except Exception as e:
        logging.error(f"Error generating test suite: {e}")
        return ""

def create_test_cases(suite_id: str, suite_description: str, test_cases: list) -> None:
    """
    Generates detailed test cases based on the provided suite ID, description, and list of test cases.
    Each test case is saved as a separate file named after its Test Case ID.

    Parameters:
        suite_id (str): The unique ID of the test suite.
        suite_description (str): The description of the test suite.
        test_cases (list): A list of dictionaries containing the test case details.
    """
    client = OpenAIApiClient()
    for test_case in test_cases:
        # Extract necessary variables from the test_case dictionary
        test_case_id = test_case.get('Test Case ID')
        description = test_case.get('Description')
        priority = test_case.get('Priority')

        if not all([test_case_id, description, priority]):
            logging.error(f"Missing required fields in test case: {test_case}")
            continue  # Skip this test case if essential fields are missing

        # Derive additional fields required by the template
        test_case_name = test_case.get('Nombre del Caso de Prueba') or description[:50]

        # Construct the variables dictionary required by the prompt template
        variables = {
            'test_case_id': test_case_id,
            'test_case_name': test_case_name,
            'description': description,
            'template_test_case': TEMPLATE_TEST_CASE,
        }

        # Render the prompt using the updated template and variables
        full_prompt = render_prompt(PROMPT_DETAILED_TEST_CASE, variables)
        logging.info(f"Creating test case for ID: {test_case_id}")
        print(f"Creating test case for ID: {test_case_id}")

        try:
            response = client.send_prompt(full_prompt)
            if response:
                # Save the test case to a file
                file_path = os.path.join(TEST_CASE_PATH, suite_id, f"{test_case_id}.md")
                ensure_directory_exists(os.path.dirname(file_path))
                save_content_to_file(file_path, response)
                logging.info(f"Test case {test_case_id} saved to {file_path}")
                print(f"Test case {test_case_id} saved to {file_path}")
            else:
                logging.error(f"Failed to generate test case {test_case_id}")
                print(f"Failed to generate test case {test_case_id}")
        except Exception as e:
            logging.error(f"Error generating test case {test_case_id}: {e}")
            print(f"Error generating test case {test_case_id}: {e}")
