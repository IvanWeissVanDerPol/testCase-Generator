### **Test Case Template: Mobile Application**

#### **Test Case ID:**
- `TC_MOB_FUNC_005`

#### **Priority:**
High

#### **Type:**
Functional

#### **Test Environment:**
iOS/Android

#### **Test Case Title:**
Verify that login fails if the user has not completed registration

#### **Description:**
This test case verifies that a user cannot log into the system if they have not completed their registration process.

#### **Preconditions:**
1. The user must be partially registered in the system (i.e., email registered, but registration not completed).
2. The application must be available and functional.  
3. Test data must be available.

#### **Test Steps:**

1. **Action**: Open the mobile application on your device  
   - **Expected Result**: The login page of the application is displayed.  
   - **Actual Result**: 

2. **Action**: Enter the email address of the partially registered user and associated password.  
   - **Expected Result**: Entered data are accepted as inputs.  
   - **Actual Result**: 

3. **Action**: Click on the 'Login' button.  
   - **Expected Result**: An error message is displayed stating that the user has not completed registration. 
   - **Actual Result**: 

#### **Expected Results:**
The user is unable to log in and receives an error message stating incomplete registration.

#### **Actual Results:**

#### **Pass/Fail:**

#### **Estimated Execution Time:**
5 minutes

#### **Screenshots/Attachments:**

#### **Notes/Comments:**
