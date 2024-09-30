### **Test Case Template: MobileApp**

#### **Test Case ID:**
- `TC_MOB_FUNC_012`

#### **Priority:**
High

#### **Type:**
Functional

#### **Test Environment:**
iOS/Android

#### **Test Case Title:**
Verify correct SMS sending for phone number validation 

#### **Description:**
This test case verifies that the mobile app correctly handles SMS sending for phone number validation. 

#### **Preconditions:**
1. The user has the mobile application installed on their device.  
2. The user has a valid phone number that can receive SMS.
3. The application has SMS sending functionality enabled.

#### **Test Steps:**

1. **Action**: Open the mobile application and navigate to the "Verify Phone Number" page.
   - **Expected Result**: The "Verify Phone Number" page is displayed.  
   - **Actual Result**: 

2. **Action**: Input a valid phone number and tap the "Verify" button.
   - **Expected Result**: An SMS containing a verification code is sent to the entered phone number.
   - **Actual Result**: 

3. **Action**: Check the received message on the phone number.
   - **Expected Result**: The text message contains a valid verification code.
   - **Actual Result**: 

#### **Expected Results:**
An SMS containing a valid verification code is successfully sent to the user's phone number.

#### **Actual Results:**

#### **Pass/Fail:**

#### **Estimated Execution Time:**
7 minutes

#### **Screenshots/Attachments:**


#### **Notes/Comments:**
Ensure the phone number used for testing can receive SMS. In case of non-receipt of SMS or invalid verification code, retry the test after some time or with a different phone number.