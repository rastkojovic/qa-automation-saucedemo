from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_multiple_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username="standard_user", password="secret_sauce")
    
    inventory_page = InventoryPage(driver)
    
    
    inventory_page.add_to_cart(By.ID, "add-to-cart-sauce-labs-backpack")
    inventory_page.add_to_cart(By.ID, "add-to-cart-sauce-labs-bike-light")
    inventory_page.add_to_cart(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    
    cart_count = inventory_page.get_cart_count()
    
    assert cart_count == "3", f"Expected cart count to be 3 but got {cart_count}"