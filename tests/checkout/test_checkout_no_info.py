from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from selenium.webdriver.common.by import By
from test_data import ERROR_FIRST_NAME

def test_checkout_no_info(driver, login_standard_user):
    """
    Test Case: TC021 - Checkout Without Provoding Any Information
    """
    
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart_page()
    
    cart_page = CartPage(driver)
    cart_page.checkout()
    
    checkout_info_page = CheckoutInfoPage(driver)
    checkout_info_page.continue_checkout()
    
    error_message_element = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    error_message = error_message_element.text
    
    assert error_message == ERROR_FIRST_NAME, f"Expected error message '{ERROR_FIRST_NAME}', but '{error_message}' is displayed"