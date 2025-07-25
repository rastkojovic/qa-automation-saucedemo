from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By
from test_data import CHECKOUT_PAGE_URL

def test_start_checkout(driver):
    """
    Test Case: TC019 - Start Checkout Process
    """
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart('Sauce Labs Onesie')
    
    inventory_page.open_cart_page()
    
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()
    
    current_url = driver.current_url
    
    assert current_url == CHECKOUT_PAGE_URL, f"Expected URL: {CHECKOUT_PAGE_URL} but got: {current_url}"