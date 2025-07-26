**Test Case ID**: TC036
**Title**: Reset App State
**Type**: Functional
**Severity**: N/A
**Precondition**: The user is logged in and is on the inventory page './inventory.html'

**Steps**:
1. Click on the 'Add to cart' button for item 'Sauce Labs Backpack'
2. Click on the 'Add to cart' button for item 'Sauce Labs Bike Light'
3. Click on the 'Add to cart' button for item 'Sauce Labs Onesie'
4. Click on the sorting dropdown menu
5. Select option 'Name (Z to A)'
6. Click on the burger menu button
7. Click on the option 'Reset App State'

**Expected result**: All items removed from cart indicated by the cart badge not being displayed and all 'Remove' buttons reverting to 'Add to cart' buttons. The sorting reverts to default option 'Name (A to Z)'

**Actual result**: The cart badge is not being displayed. All the buttons have not reverted to 'Add to cart' buttons. The sorting has not reverted to it's default option 'Name (A to Z)'

**Status**: Fail

**Note**: This functionality exist only for demonstration purposes on SauceDemo and would not be included in a production retail application. Therefore severity is marked as N/A