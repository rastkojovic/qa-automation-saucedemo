from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_remove_item_from_cart(driver):
    """
    Test Case: TC005 - Remove Item From Cart
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.remove_from_cart("Sauce Labs Backpack")
    
    cart_count = inventory_page.get_cart_count()
    
    assert cart_count == "0", f"Expected cart count to be 0 but got {cart_count}"