from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_all_items_to_cart(driver):
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    item_names = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)"
    ]
    
    inventory_page = InventoryPage(driver)
    
    for item_name in item_names:
        inventory_page.add_to_cart(item_name)
    
    cart_count = inventory_page.get_cart_count()
    
    assert cart_count == "6", f"Expected cart count to be 6 but got {cart_count}"