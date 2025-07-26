from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from test_data import ITEMS_ALPHA_ASC_VALUE

def test_reset_app_state_button(driver, login_standard_user):
    """
    Test Case: TC036 - Reset App State
    """
    
    inventory_page = InventoryPage(driver)
    
    # Change app state
    
    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Bike Light')
    inventory_page.add_to_cart('Sauce Labs Onesie')
    
    inventory_page.sort_alphabetically_descending()
    
    inventory_page.open_burger_menu()
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, "reset_sidebar_link")))
    
    # Reset app state
    
    reset_app_state_button = driver.find_element(By.ID, "reset_sidebar_link")
    reset_app_state_button.click()
    
    active_sorting_option = inventory_page.get_active_sorting_dropdown_option()
    cart_badge_num = inventory_page.get_cart_badge_num()
    
    # Check cart buttons state
    no_items_added = True
    button_elements = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for button in button_elements:
        if button.text == "Remove":
            no_items_added = False

    assert active_sorting_option == ITEMS_ALPHA_ASC_VALUE, f"Expected items to be sorted '{ITEMS_ALPHA_ASC_VALUE}' but got {active_sorting_option}"
    assert cart_badge_num == 0, f"Expected cart badge num to be 0, got {cart_badge_num}"
    assert no_items_added, f"Expected all inventory item buttons to be 'Add to cart'"
    
    
    