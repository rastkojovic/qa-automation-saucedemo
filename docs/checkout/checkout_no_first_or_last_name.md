**Test Case ID**: TC025
**Title**: Checkout Without Providing First Or Last Name
**Type**: Negative
**Severity**: Major
**Precondition**: The user has logged in, added the item 'Sauce Labs Backpack' to cart, clicked on the 'Checkout' button and is on the 'Checkout: Your Information' page './checkout-step-one.html'

**Steps**:
1. Enter postal/zip code "111111" into postal/zip code field
2. Click the 'Continue' button

**Expected result**: The error message 'Error: First Name is required' is displayed

**Actual result**: The error message 'Error: First Name is required' is displayed

**Status**: Pass