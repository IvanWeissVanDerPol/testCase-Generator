### **Test Case Template: Mobile Application**

#### **Test Case ID:**
- `TC_MOB_FUNC_002`

#### **Priority:**
High

#### **Type:**
Functional

#### **Test Environment:**
iOS/Android

#### **Test Case Title:**
Verify unsuccessful registration if the user already exists with the same email

#### **Description:**
This test case verifies that the registration process fails if a user attempts to register with an email already associated with an existing account in the system.

#### **Preconditions:**
1. A user must already be registered in the system with a specific email.
2. The mobile application must be available and functional. 
3. Test data must be available.

#### **Test Steps:**
1. **Action**: Launch the mobile application.
   - **Expected Result**: The application's main interface, containing the "Register" option, opens up.
   - **Actual Result**: 

2. **Action**: Tap on the "Register" option.
   - **Expected Result**: The registration page opens, displaying fields for entering personal information (such as email, password).
   - **Actual Result**: 

3. **Action**: Enter the test data into the respective fields, using an email address that is already associated with an existing account.
   - **Expected Result**: Data is successfully entered into all fields.
   - **Actual Result**: 

4. **Action**: Press the "Submit" button to attempt registration.
   - **Expected Result**: An error message appears notifying the user that an account already exists with the given email.
   - **Actual Result**: 

#### **Expected Results:**
Registration is unsuccessful and an appropriate error message is displayed regarding the pre-existing account with the provided email.

#### **Actual Results:**

#### **Pass/Fail:**

#### **Estimated Execution Time:**
3 minutes

#### **Screenshots/Attachments:**

#### **Notes/Comments:**
If registration fails due to network issues, retry the test.