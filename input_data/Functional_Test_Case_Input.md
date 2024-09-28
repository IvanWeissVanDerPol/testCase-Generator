# Functional Test Case Input

## 1. Introduction
This document provides input data for generating detailed functional test cases. These test cases focus on validating the functional aspects of the system, such as login, registration, and error handling processes.

## 2. Purpose
The purpose of this document is to gather input data required for creating specific, detailed test cases that ensure the proper functionality of the application's core features.

## 3. Scope
This document covers the functional test cases related to:
- User login
- Registration process
- Password recovery
- Error handling for invalid inputs

## 4. Test Case Inputs

### 4.1 Login Functionality
**Objective:** Validate that the login functionality works as expected with valid and invalid credentials.

| Test Case ID | Test Scenario                                      | Preconditions              | Test Steps                                                                 | Expected Results |
|--------------|----------------------------------------------------|----------------------------|-----------------------------------------------------------------------------|------------------|
| TC_FUNC_001  | Successful login with valid credentials            | User has valid credentials | 1. Navigate to the login page.<br>2. Enter valid username and password.<br>3. Click the login button. | User is logged in and redirected to the dashboard. |
| TC_FUNC_002  | Login with invalid password                        | User has valid username     | 1. Navigate to the login page.<br>2. Enter valid username but invalid password.<br>3. Click the login button. | Error message "Incorrect password" is displayed. |
| TC_FUNC_003  | Login with empty fields                            | None                       | 1. Navigate to the login page.<br>2. Leave both username and password fields empty.<br>3. Click the login button. | Error message "Please fill out this field" is displayed for both fields. |

### 4.2 Registration Functionality
**Objective:** Ensure that users can register with valid information and appropriate error messages are displayed for invalid inputs.

| Test Case ID | Test Scenario                                      | Preconditions              | Test Steps                                                                 | Expected Results |
|--------------|----------------------------------------------------|----------------------------|-----------------------------------------------------------------------------|------------------|
| TC_FUNC_004  | Successful registration with valid data            | None                       | 1. Navigate to the registration page.<br>2. Enter valid details for all fields.<br>3. Submit the registration form. | User is registered and redirected to the welcome page. |
| TC_FUNC_005  | Registration with missing required fields          | None                       | 1. Navigate to the registration page.<br>2. Leave required fields (e.g., email) empty.<br>3. Submit the form. | Error message "This field is required" is displayed for the empty fields. |
| TC_FUNC_006  | Registration with invalid email format             | None                       | 1. Navigate to the registration page.<br>2. Enter an invalid email format.<br>3. Submit the form. | Error message "Invalid email format" is displayed. |

### 4.3 Password Recovery
**Objective:** Validate the password recovery process for both valid and invalid inputs.

| Test Case ID | Test Scenario                                      | Preconditions              | Test Steps                                                                 | Expected Results |
|--------------|----------------------------------------------------|----------------------------|-----------------------------------------------------------------------------|------------------|
| TC_FUNC_007  | Successful password recovery with valid email      | User is registered          | 1. Navigate to the password recovery page.<br>2. Enter a registered email address.<br>3. Click "Recover Password." | A recovery email is sent to the provided email address. |
| TC_FUNC_008  | Password recovery with unregistered email          | None                       | 1. Navigate to the password recovery page.<br>2. Enter an unregistered email address.<br>3. Click "Recover Password." | Error message "Email not found" is displayed. |
| TC_FUNC_009  | Password recovery with empty email field           | None                       | 1. Navigate to the password recovery page.<br>2. Leave the email field empty.<br>3. Click "Recover Password." | Error message "Please provide an email address" is displayed. |

### 4.4 Error Handling
**Objective:** Ensure that error messages are displayed correctly for invalid input in different fields of the application.

| Test Case ID | Test Scenario                                      | Preconditions              | Test Steps                                                                 | Expected Results |
|--------------|----------------------------------------------------|----------------------------|-----------------------------------------------------------------------------|------------------|
| TC_FUNC_010  | Display error message for invalid username format  | None                       | 1. Navigate to the login page.<br>2. Enter an invalid username format.<br>3. Click the login button. | Error message "Invalid username format" is displayed. |
| TC_FUNC_011  | Display error message for incorrect password       | User has valid username     | 1. Navigate to the login page.<br>2. Enter a valid username but incorrect password.<br>3. Click the login button. | Error message "Incorrect password" is displayed. |
| TC_FUNC_012  | Display error message for empty registration fields| None                       | 1. Navigate to the registration page.<br>2. Leave all required fields empty.<br>3. Submit the form. | Error message "This field is required" is displayed for each empty field. |

## 5. Roles and Responsibilities
- **Test Lead:** Responsible for reviewing the test cases and assigning resources for execution.
- **QA Engineer:** Executes the functional test cases and reports the results.
- **Development Team:** Assists in defect resolution for any identified functional issues.

## 6. Conclusion
The functional test cases outlined in this document are essential for validating the core functionalities of the application, such as login, registration, and error handling. These cases ensure that the system behaves as expected and provides a good user experience.
