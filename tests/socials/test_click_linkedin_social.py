from pages.inventory_page import InventoryPage
from test_data import LINKEDIN_PAGE_URL

def test_click_linkedin_social(driver, login_standard_user):
    """
    Test Case: TC028 - Click On The LinkedIn Socials Link
    """
    
    inventory_page = InventoryPage(driver)
    inventory_page.open_social("linkedin")
    
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    
    current_url = driver.current_url
    
    assert current_url.startswith(LINKEDIN_PAGE_URL), f"Expected URL to be {LINKEDIN_PAGE_URL} but it is {current_url}"