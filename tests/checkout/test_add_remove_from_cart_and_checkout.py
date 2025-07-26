from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from selenium.webdriver.common.by import By
from test_data import FIRST_NAME, LAST_NAME, POSTAL_CODE, CHECKOUT_COMPLETE_URL

def test_add_remove_from_cart_and_checkout(driver, login_standard_user):
    """
    Test Case: TC031 - Add And Then Remove Items From Cart And Proceed To Checkout
    """
    
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bike Light")
    inventory_page.add_to_cart("Sauce Labs Fleece Jacket")
    inventory_page.open_cart_page()
    
    cart_page = CartPage(driver)
    cart_page.remove_from_cart("Sauce Labs Backpack")
    cart_page.remove_from_cart("Sauce Labs Bike Light")
    cart_page.remove_from_cart("Sauce Labs Fleece Jacket")
    cart_page.checkout()
    
    checkout_info_page = CheckoutInfoPage(driver)
    checkout_info_page.fill_first_name(FIRST_NAME)
    checkout_info_page.fill_last_name(LAST_NAME)
    checkout_info_page.fill_postal_code(POSTAL_CODE)
    checkout_info_page.continue_checkout()
    
    finish_button = driver.find_element(By.ID, "finish")
    finish_button.click()
    
    current_url = driver.current_url
    
    assert current_url == CHECKOUT_COMPLETE_URL, f"Expected URL: {CHECKOUT_COMPLETE_URL}, current URL: {current_url}"