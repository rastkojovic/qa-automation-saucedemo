from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from test_data import FIRST_NAME, RANDOM_CHARACTERS, POSTAL_CODE, CHECKOUT_OVERVIEW_URL

def test_invalid_format_last_name(driver, login_standard_user):
    """
    Test Case: TC033 - Providing Data In An Invalid Format For The Last Name Field
    """
    
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart_page()
    
    cart_page = CartPage(driver)
    cart_page.checkout()
    
    checkout_info_page = CheckoutInfoPage(driver)
    checkout_info_page.fill_first_name(FIRST_NAME)
    checkout_info_page.fill_last_name(RANDOM_CHARACTERS)
    checkout_info_page.fill_postal_code(POSTAL_CODE)
    checkout_info_page.continue_checkout()
    
    current_url = driver.current_url
    
    assert current_url == CHECKOUT_OVERVIEW_URL, f"Expected URL: {CHECKOUT_OVERVIEW_URL}, actual URL: {current_url}"