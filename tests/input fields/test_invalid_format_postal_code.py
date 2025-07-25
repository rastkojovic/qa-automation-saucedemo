from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from test_data import FIRST_NAME, LAST_NAME, RANDOM_CHARACTERS, CHECKOUT_OVERVIEW_URL

def test_invalid_format_postal_code(driver):
    """
    Test Case: TC034 - Providing Data In An Invalid Format For The Postal/Zip Code Field
    """
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart_page()
    
    cart_page = CartPage(driver)
    cart_page.checkout()
    
    checkout_info_page = CheckoutInfoPage(driver)
    checkout_info_page.fill_first_name(FIRST_NAME)
    checkout_info_page.fill_last_name(LAST_NAME)
    checkout_info_page.fill_postal_code(RANDOM_CHARACTERS)
    checkout_info_page.continue_checkout()
    
    current_url = driver.current_url
    
    assert current_url == CHECKOUT_OVERVIEW_URL, f"Expected URL: {CHECKOUT_OVERVIEW_URL}, actual URL: {current_url}"