from pages.login_page import LoginPage
from test_data import INVENTORY_PAGE

def test_valid_login(driver):
    """
    Test Case: TC001 - Login Using Valid Credentials For The 'Standard User'
    """

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    assert driver.current_url == INVENTORY_PAGE
    