from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

def test_click_linkedin_social(driver):
    
    LINKEDIN_PAGE_URL = "https://www.linkedin.com/company/sauce-labs/"
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    inventory_page = InventoryPage(driver)
    inventory_page.open_social("linkedin")
    
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    
    current_url = driver.current_url
    
    assert current_url.startswith(LINKEDIN_PAGE_URL), f"Expected URL to be {LINKEDIN_PAGE_URL} but it is {current_url}"