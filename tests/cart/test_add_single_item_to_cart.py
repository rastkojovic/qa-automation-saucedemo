from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    
    cart_count = inventory_page.get_cart_count()
    
    assert cart_count == "1", f"Expected cart count to be 1 but got {cart_count}"