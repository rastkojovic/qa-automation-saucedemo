from pages.inventory_page import InventoryPage
from test_data import ITEMS_ALPHA_ASC_VALUE

def test_sort_a_to_z(driver, login_standard_user):
    """
    Test Case: TC015 - Sort Inventory Items Alphabetically
    """
    
    inventory_page = InventoryPage(driver)
    inventory_page.sort_alphabetically_ascending()
    

    inventory_item_names = inventory_page.get_inventory_item_names()
    sorted_inventory_item_names = sorted(inventory_item_names)
    
    assert inventory_item_names == sorted_inventory_item_names, f"Inventory items order does not match expected {ITEMS_ALPHA_ASC_VALUE}"