**Test Case ID**: TC031
**Title**: Add And Then Remove Items From Cart And Proceed To Checkout
**Type** Negative
**Severity**: Major
**Precondition**: The user has logged in and is on the inventory page './inventory.html'

**Steps**:
1. Click on the 'Add to cart' button for the item 'Sauce Labs Backpack'
2. Click on the 'Add to cart' button for the item 'Sauce Labs Bike Light'
3. Click on 'Add to cart' button for item 'Sauce Labs Fleece Jacket'
4. Click on the cart button
5. Click on the 'Remove' button for the item 'Sauce Labs Backpack'
6. Click on the 'Remove' button for the item 'Sauce Labs Bike Light'
7. Click on the 'Remove' button for the item 'Sauce Labs Flece Jacket'
8. Click on the 'Checkout' button
9. Enter 'John' into the first name field
10. Enter 'Doe' into the last name field
11. Enter '111111' into the postal code field
12. Click the 'Continue' button
13. Click the 'Finish' button

**Expected result**: The user receives a warning or an error message when trying to checkout with an empty cart

**Actual result**: The user is allowed to complete the checkout and is redirected to 'https://www.saucedemo.com/checkout-complete.html'

**Result**: Pass (Test passes because it documents the application's current behaviour but this may be a product issue)

**Note**: This test documents that the application currently allows checkout with an empty cart which may be an unexpected or undesired behaviour. In a real-world scenario, this would be reported as a defect.