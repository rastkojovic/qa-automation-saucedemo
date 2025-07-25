from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from selenium.webdriver.common.by import By
from test_data import FIRST_NAME, LAST_NAME, POSTAL_CODE, CHECKOUT_COMPLETE_URL

def test_checkout_empty_cart(driver):
    """
    Test Case: TC030 - Checkout Empty Cart
    """
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    inventory_page = InventoryPage(driver)
    inventory_page.open_cart_page()
    
    cart_page = CartPage(driver)
    cart_page.checkout()
    
    checkout_info_page = CheckoutInfoPage(driver)
    checkout_info_page.fill_first_name(FIRST_NAME)
    checkout_info_page.fill_last_name(LAST_NAME)
    checkout_info_page.fill_postal_code(POSTAL_CODE)
    checkout_info_page.continue_checkout()
    
    finish_button = driver.find_element(By.ID, "finish")
    finish_button.click()
    
    current_url = driver.current_url
    
    assert current_url == CHECKOUT_COMPLETE_URL, f"Exptected URL: {CHECKOUT_COMPLETE_URL}, actual URL: {current_url}"