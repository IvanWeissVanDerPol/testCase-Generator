import logging
from documentation.document_generator import create_test_suite, create_test_cases, create_detailed_test_case
from context.context_manager import load_configuration
from utils.logging_setup import setup_logging

config = load_configuration()

# Set up logging
setup_logging()

def run_suite_generation(prompt: str) -> str:
    logging.info("Starting test suite generation...")
    return create_test_suite(prompt)

def run_case_generation(suite_id: str, suite_description: str) -> str:
    logging.info(f"Generating test cases for suite {suite_id}...")
    return create_test_cases(suite_id, suite_description)

def run_detailed_case_generation(case_id: str, case_description: str) -> str:
    logging.info(f"Generating detailed test case for ID: {case_id}...")
    return create_detailed_test_case(case_id, case_description)

def generate_qa_documents(suite_prompt: str, suite_id: str, suite_description: str, case_id: str, case_description: str) -> None:
    """Runs the entire QA document generation process."""
    logging.info("QA document generation process started.")
    
    suite_file_path = run_suite_generation(suite_prompt)
    
    if suite_file_path:
        case_file_path = run_case_generation(suite_id, suite_description)
        if case_file_path:
            detailed_case_content = run_detailed_case_generation(case_id, case_description)
            if detailed_case_content:
                logging.info("QA document generation process completed successfully.")
            else:
                logging.error("Failed to generate detailed test case.")
        else:
            logging.error("Failed to generate test cases.")
    else:
        logging.error("Failed to generate test suite.")
