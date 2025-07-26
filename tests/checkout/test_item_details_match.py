from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage

def test_item_details_match(driver, login_standard_user):
    """
    Test Case: TC009 - Item Details Match
    """
    
    ITEM_PAGE_URL = "https://www.saucedemo.com/inventory-item.html?id=4"
    
    inventory_page = InventoryPage(driver)
    inventory_page.open_product_page(product_name='Sauce Labs Backpack')
    
    item_name = "Sauce Labs Backpack"
    opened_item_name = driver.find_element(By.CLASS_NAME, "inventory_details_name").text
    
    assert ITEM_PAGE_URL in driver.current_url, f"URL does not match expected product page"
    assert opened_item_name == item_name, f"Expected item name 'Sauce Labs Backpack' but got {opened_item_name}"
    
    