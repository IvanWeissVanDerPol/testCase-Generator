### **Test Case Template: Mobile Banking Application**

#### **Test Case ID:**
- `TC_MOB_FUNC_010`  

#### **Priority:**
High

#### **Type:**
Functional

#### **Test Environment:**
iOS/Android

#### **Test Case Title:**
Verify that login fails if identity validation (document/face) is not completed  

#### **Description:**
This test case verifies that a user cannot log into the system if the identity validation process is not completed.

#### **Preconditions:**
1. The user must be registered in the system with valid credentials (email and password).  
2. The user did not complete the identity validation process (document verification and face verification).
3. The mobile banking application must be available and functional.
4. Test data must be available.

#### **Test Steps:**

1.  **Action**: Launch the mobile banking application  
    - **Expected Result**: The login page is displayed 
    - **Actual Result**: 

2.  **Action**: Enter valid email and password  
    - **Expected Result**: The next button becomes active
    - **Actual Result**: 

3.  **Action**: Click on the next button  
    - **Expected Result**: The user receives a notification indicating identity validation process has not been completed 
    - **Actual Result**: 

#### **Expected Results:**
The user receives a notification denying login access with a reminder to complete the identity validation.

#### **Actual Results:**
[Leave blank to be completed after test execution]

#### **Pass/Fail:**
[Leave blank to be completed after test execution]

#### **Estimated Execution Time:**
5 minutes

#### **Screenshots/Attachments:**
1. Screenshot of the Mobile Banking Application login page.
2. Screenshot of the identity validation failure notification. 

#### **Notes/Comments:**
Ensure the user has an active internet connection. If login fails due to network issues, retry the test.