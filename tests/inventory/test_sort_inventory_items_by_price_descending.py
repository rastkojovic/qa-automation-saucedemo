from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def test_sort_inventory_items_by_price_descending(driver):
    """
    Test Case: TC018 - Sort Inventory Items By Price In Descending Order
    """
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    inventory_page = InventoryPage(driver)
    item_prices = inventory_page.get_inventory_item_prices()
    reverse_sorted_prices = sorted(item_prices, reverse=True)
    
    dropdown_menu = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    dropdown_menu.select_by_visible_text("Price (high to low)")
    
    item_prices = inventory_page.get_inventory_item_prices()
    
    assert item_prices == reverse_sorted_prices, "Item prices are not sorted in descending order"