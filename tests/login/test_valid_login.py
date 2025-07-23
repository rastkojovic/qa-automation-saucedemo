from pages.login_page import LoginPage

def test_valid_login(driver):

    page = LoginPage(driver)
    page.open()
    page.login_standard_user()
    
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    