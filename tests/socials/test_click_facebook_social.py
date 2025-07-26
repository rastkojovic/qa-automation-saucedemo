from pages.inventory_page import InventoryPage
from test_data import FACEBOOK_PAGE_LINK

def test_click_facebook_social(driver, login_standard_user):
    """
    Test Case: TC027 - Click Facebook Socials Link
    """
    
    inventory_page = InventoryPage(driver)
    inventory_page.open_social("facebook")

    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    
    current_url = driver.current_url
    
    assert current_url.startswith(FACEBOOK_PAGE_LINK), f"Expected URL to be {FACEBOOK_PAGE_LINK} but it is {current_url}"