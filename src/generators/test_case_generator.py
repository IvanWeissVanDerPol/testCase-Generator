import json
import logging
import os

from api.api_caller import OpenAIApiClient

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def generate_and_save_test_cases(test_suite_path, output_root):
    try:
        # Read the test suite description
        with open(test_suite_path, 'r') as file:
            suite_description = file.read()
        
        # Generate test cases from the suite description
        client = OpenAIApiClient()
        prompt = f"""
        The following is a description of a test suite:

        {suite_description}

        Please extract all the test cases from the suite description and return them as a list of dictionaries in the following structure:

        [
            {"Test Case ID": "TC_EXAMPLE_001", "Description": "Example description", "Priority": "High", "Status": "Not executed"},
            {"Test Case ID": "TC_EXAMPLE_002", "Description": "Another example", "Priority": "Medium", "Status": "Not executed"}
        ]
        """
        response = client.send_prompt(prompt)
        test_cases = json.loads(response) if response else []
        logging.info(f"Extracted test cases: {test_cases}")
        
        # Extract suite name from the path for directory creation
        suite_name = os.path.basename(os.path.dirname(test_suite_path))
        output_dir = os.path.join(output_root, suite_name)
        create_directory(output_dir)
        
        # Save each test case to a file
        for test_case in test_cases:
            test_case_file_name = f"TestCase_{test_case['Test Case ID']}.md"
            test_case_file_path = os.path.join(output_dir, test_case_file_name)
            
            with open(test_case_file_path, 'w') as file:
                file.write(f"### **Test Case ID:** {test_case['Test Case ID']}\n")
                file.write(f"**Description:** {test_case['Description']}\n")
                file.write(f"**Priority:** {test_case['Priority']}\n")
                file.write(f"**Status:** {test_case['Status']}\n")
                
        logging.info(f"Successfully saved test cases for suite: {suite_name}")
    
    except Exception as e:
        logging.error(f"Error generating or saving test cases for suite at {test_suite_path}: {e}")

def main():
    # Define the root directory for test suites and test cases output
    test_suites_root = 'Test_Suites'
    test_cases_output_root = 'Test_Cases'
    
    # Loop through all test suites and generate corresponding test cases
    for root, dirs, files in os.walk(test_suites_root):
        for file in files:
            if file.endswith('.md'):
                test_suite_path = os.path.join(root, file)
                generate_and_save_test_cases(test_suite_path, test_cases_output_root)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()