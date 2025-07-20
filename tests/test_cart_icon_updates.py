from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By

def test_cart_icon_updates(driver):
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username="standard_user", password="secret_sauce")
    
    inventory_page = InventoryPage(driver)
    
    # Add two items to cart
    inventory_page.add_to_cart(By.ID, "add-to-cart-sauce-labs-backpack")
    inventory_page.add_to_cart(By.ID, "add-to-cart-sauce-labs-bike-light")
    
    # Remove one item form cart
    inventory_page.remove_from_cart(By.ID, "remove-sauce-labs-backpack")
    
    cart_count = inventory_page.get_cart_count()
    
    assert cart_count == "1", f"Expected cart count to be 1 but got {cart_count}"