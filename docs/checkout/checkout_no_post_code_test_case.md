**Test Case ID**: TC024
**Title** Checkout Without Providing The Postal Code
**Type**: Negative
**Severity**: Major
**Precondition**: The user has logged in, added the item 'Sauce Labs Backpack' to the cart, clicked on the 'Checkout' button and is on the 'Checkout: Your Information' page './checkout-step-one.html'

**Steps**:
1. Enter first name "John" into the first name field
2. Enter last name "Doe" into the last name field
3. Click on the 'Continue' button

**Expected result**: The error message 'Error: Postal Code is required' is displayed.

**Actual result**: The error message 'Error: Postal Code is required' is displayed.

**Status**: Pass