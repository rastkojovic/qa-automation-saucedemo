**Test Case ID**: TC023
**Title**: Checkout Without Providing The Last Name
**Type**: Negative
**Severity**: Major
**Precondition**: The user has logged in, added the item 'Sauce Labs Backpack' to cart, clicked on the 'Checkout' button and is on the 'Checkout: Your Information' page './checkout-step-one.html'

**Steps**:
1. Enter first name 'John' into the first name field
2. Enter postal/zip code '111111' into the postal/zip code field
3. Click on the 'Continue' button

**Expected result**: The error message 'Error: Last Name is required' is displayed.

**Actual result**: The error message 'Error: Last Name is required' is displayed.

**Status**: Pass