from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


def test_sort_z_to_a(driver):
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    inventory_page = InventoryPage(driver)
    inventory_page.open_sorting_dropdown()
    
    dropdown_menu = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    
    inventory_item_names = inventory_page.get_inventory_item_names()
    reversed_inventory_item_names = sorted(inventory_item_names, reverse=True)
    
    dropdown_menu.select_by_visible_text("Name (Z to A)")
    inventory_item_names = inventory_page.get_inventory_item_names()
    
    assert reversed_inventory_item_names == inventory_item_names, f"Inventory items order does not match expected (z to a)"