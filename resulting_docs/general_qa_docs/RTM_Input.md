# Requirements Traceability Matrix (RTM)

This document provides a mapping between project requirements and corresponding test cases to ensure full test coverage and traceability throughout the QA process. Each requirement is linked to relevant test cases to verify the system meets its functional and non-functional requirements.

| **Requirement ID** | **Requirement Description**          | **Test Case ID** | **Status**       | **Comments**                                                                                       |
|--------------------|--------------------------------------|------------------|------------------|----------------------------------------------------------------------------------------------------|
| REQ-001            | User Login functionality             | TC-001           | Pass             | User login functionality has been successfully tested and passed all related test cases.            |
| REQ-002            | Profile Management functionality      | TC-002           | In Progress      | Testing ongoing for profile update and management, focusing on input validation and profile saving. |
| REQ-003            | Payment Gateway integration          | TC-003           | Not Started      | Payment gateway test cases are scheduled after integration is complete.                             |
| REQ-004            | User Registration functionality      | TC-004           | Pass             | All registration test cases have passed, including email validation and account creation.           |
| REQ-005            | Password Reset functionality         | TC-005           | Pass             | Password reset functionality has been validated through multiple scenarios.                         |
| REQ-006            | Dashboard Load Performance           | NFT001           | In Progress      | Load testing is ongoing to ensure the dashboard loads within acceptable response times.             |
| REQ-007            | File Upload (5GB Stress Test)         | NFT002           | Not Started      | Stress testing for file upload is planned after basic file upload functionality is fully tested.    |
| REQ-008            | Sensitive Data Encryption            | NFT004           | In Progress      | Encryption testing for sensitive data is partially completed, focusing on passwords and payment data.|
| REQ-009            | Session Timeout (Security)           | NFT003           | Pass             | Session timeout after inactivity has been successfully validated.                                  |
| REQ-010            | Reporting Module functionality       | TC-006           | Not Started      | Test cases for report generation are yet to be executed.                                            |
| REQ-011            | Search Functionality                 | TC-007           | Pass             | Search functionality for product catalog has passed all test cases, including edge cases.           |
| REQ-012            | Browser Compatibility                | NFT009           | In Progress      | Compatibility testing for different browsers is ongoing.                                            |
| REQ-013            | API Response Time                    | NFT007           | Not Started      | API performance tests are planned for next sprint.                                                  |
| REQ-014            | User Logout Functionality             | TC-008           | Pass             | Logout functionality has been successfully tested, ensuring session termination.                    |

## Notes:
- **In Progress**: Testing is currently underway for these test cases, with partial results recorded.
- **Not Started**: These test cases are planned for future sprints.
- **Pass**: Test cases have been successfully executed and validated.

## Test Coverage Summary:
- **Functional Requirements**: All critical functional requirements are covered, with several test cases in progress or completed.
- **Non-Functional Requirements**: Performance and security requirements are partially tested, with some scheduled for the upcoming sprints.
