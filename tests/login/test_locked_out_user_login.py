from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from test_data import PASSWORD, ERROR_LOCKED_OUT

def test_locked_out_user_login(driver):
    """
    Test Case: TC011 - Login With The Credentials For The 'Locked Out User'
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username="locked_out_user", password=PASSWORD)
    
    error_message_container = driver.find_element(By.CLASS_NAME, "error-message-container")
    error_message = error_message_container.find_element(By.TAG_NAME, "h3").text
    
    assert error_message == ERROR_LOCKED_OUT, f"Expected user locked out error message but got {error_message}"