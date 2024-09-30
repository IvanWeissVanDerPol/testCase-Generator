### **Test Case Template: Mobile Application**

#### **Test Case ID:**
- `TC_MOB_FUNC_004`  

#### **Priority:**
High

#### **Type:**
Functional

#### **Test Environment:**
iOS/Android

#### **Test Case Title:**
Verify that login fails with an incorrect password

#### **Description:**
This test case verifies that a user cannot log into the system with an incorrect password.

#### **Preconditions:**
1. The user must be registered in the system with valid credentials (email and password).
2. The incorrect password for the user should be known.
3. The application is installed and functional on the mobile device (iOS/Android).
4. Test data is available.

#### **Test Steps:**

1. **Action**: Launch the application  
   - **Expected Result**: The login page is shown  
   - **Actual Result**: 

2. **Action**: Enter registered email  
   - **Expected Result**: The entered email is displayed in the email field  
   - **Actual Result**: 

3. **Action**: Enter incorrect password  
   - **Expected Result**: The entered incorrect password is displayed in the password field  
   - **Actual Result**: 

4. **Action**: Tap the Login button  
   - **Expected Result**: An error message is shown indicating incorrect password or login failure  
   - **Actual Result**: 

#### **Expected Results:**
The login attempt fails and an error message indicating incorrect password or login failure is displayed.

#### **Actual Results:**

#### **Pass/Fail:**

#### **Estimated Execution Time:**
5 minutes

#### **Screenshots/Attachments:**

#### **Notes/Comments:**
If login fail message is not displayed as expected due to network issues, retry the test.