from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_burger_menu(driver, login_standard_user):
    """
    Test Case: TC012 - Burger Menu Items Visible On Opening Burger Menu
    """
    
    inventory_page = InventoryPage(driver)
    inventory_page.open_burger_menu()
    
    burger_menu_item_names = [
        "All Items",
        "About",
        "Logout",
        "Reset App State"
    ]
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, "bm-item")))
    
    burger_menu_items = driver.find_elements(By.CLASS_NAME, "bm-item")
    burger_menu_items_str = [item.text for item in burger_menu_items]
    
    assert burger_menu_items_str == burger_menu_item_names, f"Burger menu items do not match expected content"