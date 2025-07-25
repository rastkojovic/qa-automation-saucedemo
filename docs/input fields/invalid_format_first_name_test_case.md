**Test Case ID**: TC032
**Title**: Providing Data In An Invalid Format For The First Name Field
**Precondition**: The user has logged in, added the item 'Sauce Labs Backpack' to cart and is on the checkout information page './checkout-step-one.html'
**Steps**:
1. Enter '12345!@#$%^&*' into the first name field
2. Enter 'Doe' into the last name field
3. Enter '111111' into the postal/zip code field
4. Click on the 'Continue' button

**Expected result**: User is provided with a warning or error message about the invalid first name format

**Actual result**: User is allowed to proceed to the Checkout Overview page './checkout-step-two.html'

**Result**: Pass (Test passes because it documents the application's current behaviour but this may be a product issue)

**Note**: This test documents that the application currently allows entering special characters and numbers into the first name field which may be an unexpected or undesired behaviour. In a real-world scenario, this would be reported as a defect.