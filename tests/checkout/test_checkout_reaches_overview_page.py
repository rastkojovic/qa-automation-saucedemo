from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from test_data import FIRST_NAME, LAST_NAME, POSTAL_CODE, CHECKOUT_OVERVIEW_URL

def test_checkout_reaches_overview_page(driver):
    """
    Test Case: TC020 - Checkout Reaches The Overview Page
    """
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart('Sauce Labs Onesie')
    inventory_page.open_cart_page()
    
    cart_page = CartPage(driver)
    cart_page.checkout()
    
    checkout_info_page = CheckoutInfoPage(driver)
    checkout_info_page.fill_first_name(FIRST_NAME)
    checkout_info_page.fill_last_name(LAST_NAME)
    checkout_info_page.fill_postal_code(POSTAL_CODE)
    checkout_info_page.continue_checkout()
    
    current_url = driver.current_url
    
    assert current_url == CHECKOUT_OVERVIEW_URL, f"Expected URL: {CHECKOUT_OVERVIEW_URL}, current URL: {current_url}"