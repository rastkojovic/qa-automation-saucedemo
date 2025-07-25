from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from test_data import INVALID_USERNAME, INVALID_PASSWORD


def test_invalid_login(driver):
    """
    Test Case: TC002 - Login With Invalid Credentials
    """

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username=INVALID_USERNAME, password=INVALID_PASSWORD)
    
    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    
    assert error_message.is_displayed()
    