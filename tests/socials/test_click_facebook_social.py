from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from test_data import FACEBOOK_PAGE_LINK

def test_click_facebook_social(driver):
    """
    Test Case: TC027 - Click Facebook Socials Link
    """
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    inventory_page = InventoryPage(driver)
    inventory_page.open_social("facebook")

    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    
    current_url = driver.current_url
    
    assert current_url.startswith(FACEBOOK_PAGE_LINK), f"Expected URL to be {FACEBOOK_PAGE_LINK} but it is {current_url}"