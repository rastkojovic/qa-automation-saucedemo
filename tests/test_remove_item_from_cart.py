from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_remove_item_from_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username="standard_user", password="secret_sauce")
    
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart(By.ID, "add-to-cart-sauce-labs-backpack")
    inventory_page.remove_from_cart(By.ID, "remove-sauce-labs-backpack")
    
    cart_count = inventory_page.get_cart_count()
    
    assert cart_count == "0", f"Expected cart count to be 0 but got {cart_count}"