from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from selenium.webdriver.common.by import By
from test_data import FIRST_NAME, ERROR_LAST_NAME

def test_checkout_no_last_name(driver, login_standard_user):
    """
    Test Case: TC023 - Checkout Without Providing The Last Name
    """
    
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart_page()
    
    cart_page = CartPage(driver)
    cart_page.checkout()
    
    checkout_info_page = CheckoutInfoPage(driver)
    checkout_info_page.fill_first_name(FIRST_NAME)
    checkout_info_page.continue_checkout()
    
    error_message_element = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    error_message = error_message_element.text
    
    assert error_message == ERROR_LAST_NAME, f"Expected error message '{ERROR_LAST_NAME}', but '{error_message}' is displayed"