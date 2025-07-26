from pages.inventory_page import InventoryPage
from test_data import ITEMS_NUM_ASC_VALUE

def test_sort_inventory_items_by_price(driver, login_standard_user):
    """
    Test Case: TC017 - Sort Inventory Items By Price In Ascending Order
    """
    
    inventory_page = InventoryPage(driver)
    price_list = inventory_page.get_inventory_item_prices()
    sorted_price_list = sorted(price_list)
    
    inventory_page.sort_by_price_ascending()
    
    price_list = inventory_page.get_inventory_item_prices()
    
    assert price_list == sorted_price_list, f"Inventory items order does not match expected {ITEMS_NUM_ASC_VALUE}"