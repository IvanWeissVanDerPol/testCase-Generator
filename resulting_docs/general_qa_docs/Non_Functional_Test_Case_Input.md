# Non-Functional Test Case Input

This document focuses on testing non-functional aspects of the system, including performance, usability, and security. Non-functional test cases ensure that the system meets performance standards, usability criteria, and security requirements.

## Key Non-Functional Test Cases

| **Test Case ID** | **Test Name**                        | **Objective**                                                | **Test Description**                                               | **Expected Outcome**                                                        | **Tool**         | **Priority**  | **Dependencies**                                       | **Test Environment**                                                                                                                                               |
|------------------|--------------------------------------|--------------------------------------------------------------|-------------------------------------------------------------------|------------------------------------------------------------------------------|------------------|---------------|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFT001            | Load Test for User Dashboard         | Validate system performance under load.                      | Test with 1000 concurrent users accessing the dashboard.           | - Dashboard load time must be within 2 seconds.                              | JMeter           | High          | - User database with at least 1000 test users.<br> - Dashboard must be deployed. | **OS**: Windows 10, macOS 12.x<br> **Network**: High-speed internet<br> **Database**: MySQL (version 8.x)                                                          |
| NFT002            | Stress Test for File Upload          | Test system stability under stress.                          | Upload a 5GB file to test the system’s ability to handle stress.   | - System remains responsive.<br> - No crashes or significant slowdowns.      | LoadRunner       | High          | - File upload feature must be deployed.               | Same as above                                                                                                                                                       |
| NFT003            | User Session Timeout                 | Validate session management security.                        | Verify that user sessions are automatically terminated after 10 minutes of inactivity. | - User session ends after 10 minutes of inactivity.<br> - User is prompted to log in again. | Burp Suite       | Medium        | - Active session must be maintained.                  | Same as above                                                                                                                                                       |
| NFT004            | Sensitive Data Encryption            | Ensure sensitive data security.                              | Verify that sensitive user data (e.g., passwords) is encrypted in transit and at rest. | - All sensitive data is encrypted using industry-standard encryption (e.g., AES-256).<br> - Data cannot be accessed or viewed in plaintext. | Burp Suite       | Critical       | - User data must include sensitive information.<br> - Encryption mechanism must be implemented. | Same as above                                                                                                                                                       |
| NFT005            | Usability Test for User Dashboard    | Evaluate ease of use and user experience.                    | Conduct a usability study to assess the user-friendliness of the dashboard UI. | - User feedback is positive, indicating a smooth and intuitive user experience. | Morae            | Medium        | - User dashboard must be deployed.<br> - Usability participants must be available. | Same as above                                                                                                                                                       |
| NFT006            | Load Test for Search Functionality   | Ensure search feature performs under heavy load.             | Test with 500 concurrent users performing searches simultaneously. | - Search results are displayed within 3 seconds.<br> - No significant slowdowns or errors. | JMeter           | Medium        | - Product catalog must be updated.<br> - Search index must be functional. | Same as above                                                                                                                                                       |
| NFT007            | Response Time for API Requests       | Measure the response time of critical API endpoints.         | Send multiple concurrent requests to API endpoints.                | - API responses must be received within 1 second under load.                  | Postman, JMeter  | High          | - API endpoints must be deployed.                     | Same as above                                                                                                                                                       |
| NFT008            | Security Vulnerability Assessment    | Identify potential vulnerabilities in the system.            | Perform a thorough security assessment of all critical modules.    | - No critical vulnerabilities are found.<br> - System complies with OWASP security guidelines. | OWASP ZAP        | Critical       | - System must be fully deployed.<br> - All modules must be accessible for scanning. | Same as above                                                                                                                                                       |

### Additional Non-Functional Test Cases

| **Test Case ID** | **Test Name**                   | **Objective**                                                | **Test Description**                                              | **Expected Outcome**                                                | **Tool**         | **Priority**  | **Dependencies**                                    | **Test Environment**                                                                                                                                           |
|------------------|---------------------------------|--------------------------------------------------------------|------------------------------------------------------------------|--------------------------------------------------------------------|------------------|---------------|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFT009            | Browser Compatibility Testing   | Verify that the application is compatible with multiple browsers. | Test the application on Chrome, Firefox, Safari, and Edge.         | - Application works smoothly across all supported browsers.        | Selenium         | Medium        | - Supported browsers must be available.           | **Browsers**: Chrome, Firefox, Safari, Edge<br> **OS**: Windows, macOS                                                                                         |
| NFT010            | Load Test for Login Page        | Ensure login page handles high user loads.                    | Test with 1000 concurrent users attempting to log in simultaneously. | - Login page remains responsive and loads within 2 seconds.         | JMeter           | High          | - User accounts must exist for login testing.     | Same as above                                                                                                                                                  |
| NFT011            | System Recovery Test            | Test system's ability to recover from crashes or failures.    | Simulate system crashes or database failures and observe recovery. | - System recovers within acceptable time frames without data loss. | LoadRunner       | Critical       | - System must be configured to support failover.  | Same as above                                                                                                                                                  |

## Test Data:

1. **Load Test for User Dashboard**: 
   - Test with 1000 test user accounts.
2. **Stress Test for File Upload**: 
   - 5GB test file.
3. **Sensitive Data Encryption**: 
   - User password: `P@ssw0rd!`, Credit Card Number: `4111111111111111`
4. **Load Test for Search Functionality**: 
   - Search query: "Laptop"

## Test Environment:

- **Operating System**:
  - Windows 10
  - macOS 12.x
- **Browser**:
  - Chrome (latest version)
  - Firefox (latest version)
  - Safari (latest version for macOS)
  - Microsoft Edge (latest version)
- **Database**:
  - MySQL (version 8.x)
- **Network Conditions**:
  - Tests will be conducted under stable, high-speed conditions and under low-bandwidth constraints to simulate real-world scenarios.
  
## Defect Handling:

- Any defects identified during non-functional testing will be logged and tracked using **JIRA**.
- Defects will be categorized based on their impact on performance, usability, or security (Critical, Major, Minor).

## Reporting:

- Detailed reports will be generated at the completion of each test, providing insights into system performance, usability, and security.
- Reports will highlight any bottlenecks, vulnerabilities, or areas requiring improvement, with a focus on resolving critical issues before the next release.

## Continuous Improvement:

- Performance and security reviews will be conducted after each major release to assess system improvements.
- Test results will be analyzed to identify recurring issues and optimize system performance and security for future releases.
