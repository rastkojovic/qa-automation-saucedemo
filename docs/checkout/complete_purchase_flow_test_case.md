**Test Case ID**: TC026
**Title** Complete Purchase Flow
**Type**: End-To-End
**Severity**: Critical
**Preconditions**: The user is on the saucedemo website page 'https://www.saucedemo.com/'

**Steps**:
1. Enter 'standard_user' into the username field
2. Enter 'secret_sauce' into the password field
3. Click the 'Login' button
4. Click the 'Add to cart' button for the item 'Sauce Labs Backpack'
5. Click on the cart button
6. Click on the 'Checkout' button
7. Enter 'John' into the first name field
8. Enter 'Doe' into the last name field
9. Enter '111111' into the postal/zip code field
11. Click on the 'Continue' button
12. Click on the 'Finish' button

**Expected result**: The user is redirected to the checkout complete page './checkout-complete.html'

**Actual result**: The user is redirected to the checkout complete page './checkout-complete.html'

**Result**: Pass