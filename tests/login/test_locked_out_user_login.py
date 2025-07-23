from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_locked_out_user_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username="locked_out_user", password="secret_sauce")
    
    error_message_container = driver.find_element(By.CLASS_NAME, "error-message-container")
    error_message = error_message_container.find_element(By.TAG_NAME, "h3").text
    
    assert error_message == "Epic sadface: Sorry, this user has been locked out.", f"Expected user locked out error message but got {error_message}"