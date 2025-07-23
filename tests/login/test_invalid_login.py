from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

INVALID_USERNAME = "invalid-username"
INVALID_PASSWORD = "invalid-password"
URL = "https://www.saucedemo.com"

def test_invalid_login(driver):

    page = LoginPage(driver)
    page.open()
    page.login(username=INVALID_USERNAME, password=INVALID_PASSWORD)
    
    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    
    assert error_message.is_displayed()
    