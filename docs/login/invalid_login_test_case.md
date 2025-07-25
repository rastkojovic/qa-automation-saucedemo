**Test Case ID**: TC002
**Test Type**: Functional
**Priority**: High
**Title**: Login With Invalid Credentials
**Precondition**: User has invalid credentials and is on the login page.
**Steps**:
1. Go to: 'https://www.saucedemo.com'
2. Enter username: "invalid-username"
3. Enter password: "invalid-password"
4. Click on the login button

**Expected result**:
User is unable to login. The error message "Epic sadface: Username and password do not match any user in this service" is displayed.

**Actual result**:
User is unable to login. The error message "Epic sadface: Username and password do not match any user in this service" is displayed.

**Status**: Pass