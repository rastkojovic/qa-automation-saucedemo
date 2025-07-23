from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_item_details_match(driver):
    
    item_page_url = "https://www.saucedemo.com/inventory-item.html?id=4"
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    inventory_page = InventoryPage(driver)
    inventory_page.open_product_page(product_name='Sauce Labs Backpack')
    
    item_name = "Sauce Labs Backpack"
    opened_item_name = driver.find_element(By.CLASS_NAME, "inventory_details_name").text
    
    assert item_page_url in driver.current_url, f"URL does not match expected product page"
    assert opened_item_name == item_name, f"Expected item name 'Sauce Labs Backpack' but got {opened_item_name}"
    
    