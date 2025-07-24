**Test Case ID**: TC022
**Title**: Checkout no first name
**Precondition**: The user has logged in, added item 'Sauce Labs Backpack' to cart, clicked on 'Checkout' button and is on the 'Checkout: Your Information' page './checkout-step-one.html'
**Steps**:
1. Enter last name 'Doe' into the last name field
2. Enter postal/zip code '111111' into postal/zip code field
3. Click on 'Continue' button

**Expected result**: The error message 'Error: First Name is required' is displayed.

**Actual result**: The error message 'Error: First Name is required' is displayed.

**Result**: Pass