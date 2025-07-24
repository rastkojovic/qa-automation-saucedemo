**Test Case ID**: TC023
**Title**: Checkout no last name
**Precondition**: The user has logged in, added item 'Sauce Labs Backpack' to cart, clicked on 'Checkout' button and is on the 'Checkout: Your Information' page './checkout-step-one.html'
**Steps**:
1. Enter first name 'John' into first name field
2. Enter postal/zip code '111111' into postal/zip code field
3. Click on 'Continue' button

**Expected result**: Error message 'Error: Last Name is required' is displayed.

**Actual result**: Error message 'Error: Last Name is required' is displayed.

**Result**: Pass