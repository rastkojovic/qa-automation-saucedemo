from test_data import INVENTORY_PAGE_URL

def test_valid_login(driver, login_standard_user):
    """
    Test Case: TC001 - Login Using Valid Credentials For The 'Standard User'
    """
    current_url = driver.current_url
    assert current_url == INVENTORY_PAGE_URL, f"Expected URL '{INVENTORY_PAGE_URL}', got '{current_url}'"
    