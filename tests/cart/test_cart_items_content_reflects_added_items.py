from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage 
from pages.cart_page import CartPage

def test_cart_items_content_reflects_added_items(driver):
    """
    Test Case: TC010 - Cart Item's Content Reflects Added Items
    """
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    inventory_page = InventoryPage(driver)
    
    item_names = [
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)",
        "Sauce Labs Bike Light"
    ]
    
    
    for item_name in item_names:
        inventory_page.add_to_cart(item_name)
        
    cart_page = CartPage(driver)
    cart_page.open()
    cart_items = cart_page.get_cart_items()
    cart_items_str = [item.text for item in cart_items]
    
    assert cart_items_str == item_names, f"The cart items do not match items added to cart"
    
    