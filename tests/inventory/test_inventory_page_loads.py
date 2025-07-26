from pages.inventory_page import InventoryPage

def test_inventory_page_loads(driver, login_standard_user):
    """
    Test Case: TC003 - Inventory Page Loads After Login
    """
    
    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded()