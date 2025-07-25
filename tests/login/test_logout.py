from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from test_data import SAUCEDEMO_URL


def test_logout(driver):
    """
    Test Case: TC013 - Logout Test
    """
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    inventory_page = InventoryPage(driver)
    inventory_page.open_burger_menu()
    
    logout_btn_selector = ".bm-item-list a:nth-child(3)"
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, logout_btn_selector)))
    
    logout_button = driver.find_element(By.CSS_SELECTOR, logout_btn_selector)
    logout_button.click()
    
    current_url = driver.current_url
    assert current_url == SAUCEDEMO_URL, f"Current URL {current_url} does not match expected URL {SAUCEDEMO_URL}"