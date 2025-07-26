from pages.inventory_page import InventoryPage
from test_data import ITEMS_ALPHA_DESC_VALUE


def test_sort_z_to_a(driver, login_standard_user):
    """
    Test Case: TC016 - Sort Inventory Items In A Reverse Alphabetical Order
    """
    
    inventory_page = InventoryPage(driver)
    
    inventory_item_names = inventory_page.get_inventory_item_names()
    reversed_inventory_item_names = sorted(inventory_item_names, reverse=True)
    
    inventory_page.sort_alphabetically_descending()
    inventory_item_names = inventory_page.get_inventory_item_names()
    
    assert reversed_inventory_item_names == inventory_item_names, f"Inventory items order does not match expected {ITEMS_ALPHA_DESC_VALUE}"