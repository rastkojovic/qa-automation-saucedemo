from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory_page_loads(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username="standard_user", password="secret_sauce")
    
    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded()