from pages.login_page import LoginPage

USERNAME = "standard_user"
PASSWORD = "secret_sauce"
URL = "https://www.saucedemo.com"
    

def test_valid_login(driver):

    page = LoginPage(driver)
    page.open()
    page.login(username=USERNAME, password=PASSWORD)
    
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    