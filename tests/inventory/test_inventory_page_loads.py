from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory_page_loads(driver):
    """
    Test Case: TC003 - Inventory Page Loads After Login
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded()