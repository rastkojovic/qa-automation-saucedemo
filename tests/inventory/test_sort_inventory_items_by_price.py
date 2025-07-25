from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

def test_sort_inventory_items_by_price(driver):
    """
    Test Case: TC017 - Sort Inventory Items By Price In Ascending Order
    """
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    inventory_page = InventoryPage(driver)
    price_list = inventory_page.get_inventory_item_prices()
    sorted_price_list = sorted(price_list)
    
    inventory_page.open_sorting_dropdown()
    dropdown_menu = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    dropdown_menu.select_by_visible_text("Price (low to high)")
    
    price_list = inventory_page.get_inventory_item_prices()
    
    assert price_list == sorted_price_list, f"Inventory items not sorted by prices in ascending order"