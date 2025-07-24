from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

def test_reset_app_state_button(driver):
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    inventory_page = InventoryPage(driver)
    inventory_page.open_burger_menu()
    
    # TODO: You need to change the app state first!!!
    
    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Bike Light')
    inventory_page.add_to_cart('Sauce Labs Onesie')
    
    # TODO: Add methods for sorting by every critera
    inventory_page.open_sorting_dropdown()
    
    reset_app_state_button_locator = (By.ID, "reset_sidebar_link")
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(reset_app_state_button_locator))
    
    reset_app_state_button = driver.find_element(reset_app_state_button_locator)
    reset_app_state_button.click()
    
    # TODO: If cart is empty this element will not be found!!
    cart_badge_num = inventory_page.get_cart_badge_num()
    active_sorting_option = inventory_page.get_active_sorting_dropdown_option()
    
    
    