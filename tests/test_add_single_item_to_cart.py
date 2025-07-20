from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By

def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart(By.ID, "add-to-cart-sauce-labs-backpack")
    
    cart_count = inventory_page.get_cart_count()
    
    assert cart_count == "1", f"Expected cart count to be 1 but got {cart_count}"