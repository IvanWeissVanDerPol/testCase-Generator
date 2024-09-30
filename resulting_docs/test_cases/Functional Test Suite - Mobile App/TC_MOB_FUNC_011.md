### **Test Case Template: Mobile Application**

#### **Test Case ID:**
- `TC_MOB_FUNC_011`

#### **Priority:**
High

#### **Type:**
Functional

#### **Test Environment:**
iOS/Android

#### **Test Case Title:**
Verify that a user cannot register with the same email for two accounts

#### **Description:**
This test case verifies that a user can't register a second account with a duplicated email that's already registered.

#### **Preconditions:**
1. The user must have already been registered in the system with valid credentials (email and password).
2. The application must be available and functional.
3. The user has a second unregistered email.

#### **Test Steps:**

1. **Action**: Launch the app and navigate to the registration page.  
   - **Expected Result**: The registration form is displayed.  
   - **Actual Result**: 

2. **Action**: Enter the details (First Name, Last Name, password, etc.), but enter the email that's already registered for a previous account.  
   - **Expected Result**: Once the same email is entered, an error/warning message should be displayed.  
   - **Actual Result**: 

3. **Action**: Continue the Registration attempt with the same (previously registered) email.  
   - **Expected Result**: The system blocks the registration, maintains the error message and does not allow the user to proceed with the attempt.  
   - **Actual Result**: 

#### **Expected Results:**
The system does not allow the registration to proceed with the already registered email. An error/warning message is continuously displayed.

#### **Actual Results:**

#### **Pass/Fail:**

#### **Estimated Execution Time:**
5 minutes

#### **Screenshots/Attachments:**
1. Screenshot of the duplicated email error message.

#### **Notes/Comments:**
It's important that this test case includes the scenario in which the user continues to attempt registration despite seeing the error message.