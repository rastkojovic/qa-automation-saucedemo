from pages.inventory_page import InventoryPage
from test_data import ITEMS_NUM_DESC_VALUE

def test_sort_inventory_items_by_price_descending(driver, login_standard_user):
    """
    Test Case: TC018 - Sort Inventory Items By Price In Descending Order
    """
    
    inventory_page = InventoryPage(driver)
    item_prices = inventory_page.get_inventory_item_prices()
    reverse_sorted_prices = sorted(item_prices, reverse=True)
    
    inventory_page.sort_by_price_descending()
    
    item_prices = inventory_page.get_inventory_item_prices()
    
    assert item_prices == reverse_sorted_prices, f"Inventory items order does not match expected {ITEMS_NUM_DESC_VALUE}"