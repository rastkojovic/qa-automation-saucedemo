**Test Case ID**: TC030
**Title**: Checkout Empty Cart
**Type** Negative
**Precondition**: The user has logged in and is on the inventory page './inventory.html'
**Steps**:
1. Click on the cart button
2. Click on the 'Checkout' button on the cart page './cart.html'
3. Enter first name 'John' into the username field
4. Enter last name 'Doe' into the password field
5. Enter postal code '111111' into the postal code field
6. Click on the 'Continue' button
7. Click on the 'Finish' button

**Expected result**: User is provided with a warning or error message

**Actual result** The user is allowed to checkout and is redirected to './checkout-complete.html'

**Result**: Pass (Test passes because it documents the application's current behaviour but this may be a product issue)

**Note**: This test documents that the application currently allows checkout with an empty cart which may be an unexpected or undesired behaviour. In a real-world scenario, this would be reported as a defect.