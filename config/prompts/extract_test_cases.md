You are provided with a test suite description below:

{{ suite_description }}

Your task is to extract all test cases explicitly mentioned in this suite description. Format the extracted test cases as a list of dictionaries, with each dictionary representing a single test case following this structure:

- **Test Case ID**: A unique identifier for the test case (e.g., "TC_GENERIC_001").
- **Description**: A brief description of what the test case verifies (e.g., "Verify successful user registration with valid data").
- **Priority**: The test case's level of importance (e.g., "High", "Medium", "Low").
- **Status**: The current status of the test case (e.g., "Not executed", "In progress").
- **Test Environment**: Specify the environment where the test should be executed (e.g., "iOS", "Android", "Web").

Ensure the following:
1. **Relevance**: Include only those test cases explicitly mentioned in the suite description.
2. **Variants**: Capture all variants of the test case (positive, negative, and edge cases) where applicable.
3. **Format**: Strictly follow the provided structure.
4. **Completeness**: Ensure all described test cases are included in the output list.

Only provide the JSON list of test cases, and no additional text.
