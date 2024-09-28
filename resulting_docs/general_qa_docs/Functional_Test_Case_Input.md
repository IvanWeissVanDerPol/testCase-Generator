# Functional Test Case Input

This document provides comprehensive input for functional test cases designed to validate the system against its functional requirements. It includes key functional areas of the application, test data, test environments, and expected outcomes to ensure that the system behaves as expected.

## Key Functional Test Cases

| **Test Case ID** | **Test Name**             | **Objective**                                                       | **Input**                               | **Steps**                                                                                                                                                               | **Expected Outcome**                                                                                                                                                      | **Priority** | **Dependencies**                                           | **Test Environment**                                                                                                                                                                         |
|------------------|---------------------------|---------------------------------------------------------------------|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC001            | Login Functionality        | Verify that users can log in with valid credentials.                | Username, Password                      | 1. Navigate to the login page.<br> 2. Enter valid username and password.<br> 3. Click "Login".                                                                         | - Redirects user to dashboard if successful.<br> - Error message ("Invalid username or password") for invalid credentials.                                                  | High         | - User account must exist in the database.<br> - User must have appropriate access rights. | **OS**: Windows 10, macOS 12.x<br> **Browser**: Chrome (latest), Firefox (latest), Safari (latest for macOS)<br> **Database**: MySQL (version 8.x)<br> **Network**: Stable and low-bandwidth |
| TC002            | User Profile Update        | Ensure users can update their profile information.                  | Profile details (name, address, phone)  | 1. Navigate to user profile page.<br> 2. Edit profile details (e.g., name, address, phone).<br> 3. Click "Save".                                                       | - Profile details are saved successfully.<br> - Confirmation message ("Profile updated successfully").                                                                     | Medium       | - User must be logged in.<br> - Data format for phone and address must be validated. | Same as above                                                                                                                                                                                |
| TC003            | Password Reset Functionality | Validate the password reset feature for account recovery.           | Registered email address                | 1. Navigate to "Forgot Password" page.<br> 2. Enter registered email.<br> 3. Click "Submit".<br> 4. Follow password reset instructions from email.                      | - Password reset link sent to the registered email.<br> - User can successfully reset password using the link.                                                             | High         | - User email must exist in the system.<br> - Email service must be operational.     | Same as above                                                                                                                                                                                |
| TC004            | Product Search Functionality | Verify that users can search for products using keywords.            | Product name or category                | 1. Navigate to the search bar.<br> 2. Enter a product name or category (e.g., "Laptop").<br> 3. Click "Search".                                                        | - System displays relevant product results based on the search term.                                                                                                      | Medium       | - Product catalog must be up to date.<br> - Search index should be functional.     | Same as above                                                                                                                                                                                |
| TC005            | Checkout Process           | Ensure users can complete a purchase.                               | Selected product, shipping details, payment method | 1. Add products to the cart.<br> 2. Proceed to checkout.<br> 3. Enter shipping details and payment method.<br> 4. Confirm the purchase.                                   | - Order is successfully placed.<br> - Confirmation email is sent to the user.                                                                                            | High         | - Payment gateway must be operational.<br> - Products must be in stock.          | Same as above                                                                                                                                                                                |

### Additional Functional Test Cases:

| **Test Case ID** | **Test Name**                | **Objective**                                                        | **Input**                                   | **Steps**                                                                                                                                                            | **Expected Outcome**                                                                                                               | **Priority** | **Dependencies**                                           | **Test Environment**                                                                                                                                                                         |
|------------------|------------------------------|----------------------------------------------------------------------|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|--------------|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC006            | Logout Functionality          | Verify that users can log out of the system successfully.             | Logged in user session                      | 1. Navigate to the user menu.<br> 2. Click "Logout".                                                                                                                | - User is logged out, and the login page is displayed.<br> - Session is terminated.                                                | Medium       | - User must be logged in.<br> - Active session required.    | Same as above                                                                                                                                                                                |
| TC007            | Add Product to Cart           | Validate that users can add products to their shopping cart.          | Product selection                           | 1. Navigate to a product page.<br> 2. Click "Add to Cart".                                                                                                          | - Product is added to the cart.<br> - Cart displays correct product information (name, price, quantity).                       | High         | - Product must be available in inventory.                   | Same as above                                                                                                                                                                                |
| TC008            | Remove Product from Cart      | Verify that users can remove items from their shopping cart.          | Selected product in cart                    | 1. Open the shopping cart.<br> 2. Click "Remove" on the selected product.                                                                                           | - Product is removed from the cart.<br> - Cart is updated to reflect changes.                                                    | Medium       | - Product must be added to the cart before removal.        | Same as above                                                                                                                                                                                |
| TC009            | Apply Discount Code           | Ensure users can apply a discount code at checkout.                   | Valid discount code                         | 1. Navigate to the checkout page.<br> 2. Enter a valid discount code in the "Discount" field.<br> 3. Click "Apply".                                                | - Discount is applied, and total price is updated accordingly.                                                                  | Medium       | - Valid discount code must exist in the system.            | Same as above                                                                                                                                                                                |
| TC010            | View Order History            | Validate that users can view their order history after making a purchase. | Logged in user, completed order             | 1. Navigate to the user profile.<br> 2. Click "Order History".                                                                                                      | - Order history displays all past purchases, including product details, dates, and order status.                               | Low          | - User must have made a previous purchase.                   | Same as above                                                                                                                                                                                |

## Test Data:

1. **Login Test**: 
   - Username: `testuser1`
   - Password: `Test@123`
2. **User Profile Update**: 
   - Name: `John Doe`
   - Address: `123 Main St, City, Country`
   - Phone: `+1234567890`
3. **Password Reset**: 
   - Email: `testuser1@example.com`
4. **Product Search**: 
   - Keyword: `Laptop`
5. **Checkout Process**: 
   - Product: `Dell Inspiron 15`
   - Payment Method: `Visa`
6. **Add Product to Cart**: 
   - Product: `Dell Inspiron 15`
7. **Apply Discount Code**: 
   - Discount Code: `SAVE10`

## Test Environment:

- **Operating System**:
  - Windows 10
  - macOS 12.x
- **Browser**:
  - Chrome (latest version)
  - Firefox (latest version)
  - Safari (latest version for macOS)
- **Database**:
  - MySQL (version 8.x)
- **Network Conditions**:
  - Tests to be executed in both stable and low-bandwidth environments to simulate real-world conditions.

## Defect Handling:

- Any defects found during the execution of these functional tests will be logged and tracked using **JIRA**.
- Defects will be categorized by **severity** (Critical, Major, Minor) and **priority** (P1, P2, P3) for resolution.

## Reporting:

- Weekly reports will be generated to highlight open defects, their current statuses, and risk levels.
- These reports will be shared with stakeholders, including developers, project managers, and QA leads, to ensure transparency and prompt attention to high-risk areas.

## Continuous Improvement:

- Post-release reviews will be conducted to identify the root causes of major defects.
- Lessons learned will be incorporated into future testing cycles to improve the overall quality of defect management and reduce project risks.
