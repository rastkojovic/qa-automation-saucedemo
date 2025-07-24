from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_click_twitter_social(driver):
    
    # The intent is to open X (formerly Twitter) which it does indirectly through redirection
    TWITTER_PAGE_URL = "https://x.com/saucelabs"
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    inventory_page = InventoryPage(driver)
    
    inventory_page.open_social("twitter")
    
    WebDriverWait(driver, 15).until(expected_conditions.number_of_windows_to_be(2))
    
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    
    current_url = driver.current_url
    
    assert current_url.startswith(TWITTER_PAGE_URL), f"Expected the URL to be '{TWITTER_PAGE_URL}' but it is {current_url}"