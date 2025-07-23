from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


def test_logout(driver):
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    inventory_page = InventoryPage(driver)
    inventory_page.open_burger_menu()
    
    logout_btn_selector = ".bm-item-list a:nth-child(3)"
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, logout_btn_selector)))
    
    logout_button = driver.find_element(By.CSS_SELECTOR, logout_btn_selector)
    logout_button.click()
    
    url = driver.current_url
    assert url == "https://www.saucedemo.com/", f"Current URL {url} does not match expected URL https://www.saucedemo.com/"