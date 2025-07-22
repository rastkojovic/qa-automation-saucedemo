from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_sort_a_to_z(driver):
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    inventory_page = InventoryPage(driver)
    inventory_page.open_sorting_dropdown()
    
    sorting_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sorting_dropdown.select_by_visible_text("Name (A to Z)")
    
    inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    inventory_item_names = [item.text for item in inventory_items]
    sorted_inventory_item_names = sorted(inventory_item_names)
    
    assert inventory_item_names == sorted_inventory_item_names, f"Inventory items are not sorted alphabetically (a to z)"