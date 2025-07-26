from pages.inventory_page import InventoryPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_data import TWITTER_PAGE_URL

def test_click_twitter_social(driver, login_standard_user):
    """
    Test Case: TC029 - Click On The Twitter Socials Link
    """
    
    # Note: The intent is to open X (formerly Twitter) which it does indirectly through redirection
    
    inventory_page = InventoryPage(driver)
    
    inventory_page.open_social("twitter")
    
    WebDriverWait(driver, 5).until(expected_conditions.number_of_windows_to_be(2))
    
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    
    current_url = driver.current_url
    
    assert current_url.startswith(TWITTER_PAGE_URL), f"Expected the URL to be '{TWITTER_PAGE_URL}' but it is {current_url}"