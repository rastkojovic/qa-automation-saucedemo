from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_multiple_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    inventory_page = InventoryPage(driver)
    
    item_names = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt"
    ]
    
    for item_name in item_names:
        inventory_page.add_to_cart(item_name)
    
    cart_count = inventory_page.get_cart_count()
    
    assert cart_count == "3", f"Expected cart count to be 3 but got {cart_count}"