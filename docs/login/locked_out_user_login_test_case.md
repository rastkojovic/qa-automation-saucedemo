**Test Case ID**: TC011
**Title**: Login With The Credentials For The 'Locked Out User'
**Type**: Negative
**Severity**: Major
**Precondition**: The user is on the login page 'https://www.saucedemo.com/'

**Steps**:
1. Enter username 'locked_out_user'
2. Enter password 'secret_sauce'
3. Click on the 'Login' button

**Expected result**: User recieves the error message 'Epic sadface: Sorry, this user has been locked out.' and is unable to log in.

**Actual result**: User recieves the error message 'Epic sadface: Sorry, this user has been locked out.' and is unable to log in.

**Result**: Pass