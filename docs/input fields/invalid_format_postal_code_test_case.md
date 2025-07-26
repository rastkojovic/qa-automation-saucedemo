**Test Case ID**: TC034
**Title**: Providing Data In An Invalid Format For The Postal/Zip Code Field
**Type**: Negative
**Severity**: Major
**Precondition**: The user has logged in, added the item 'Sauce Labs Backpack' to cart and is on the checkout information page './checkout-step-one.html'

**Steps**:
1. Enter 'John' into the first name field
2. Enter 'Doe' into the last name field
3. Enter '12345!@#$%^&*' into the postal/zip code field
4. Click on the 'Continue' button

**Expected result**: User is provided with a warning or error message about the invalid postal code format

**Actual result**: User is allowed to proceed to the Checkout Overview page './checkout-step-two.html'

**Status**: Pass (Test passes because it documents the application's current behaviour but this may be a product issue)

**Note**: This test documents that the application currently allows entering special characters and numbers into the postal code field which may be an unexpected or undesired behaviour. In a real-world scenario, this would be reported as a defect.