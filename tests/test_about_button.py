from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_about_button(driver):
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_standard_user()
    
    inventory_page = InventoryPage(driver)
    inventory_page.open_burger_menu()
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, "about_sidebar_link")))
    
    about_button = driver.find_element(By.ID, "about_sidebar_link")
    about_button.click()
    
    url = driver.current_url
    assert url == "https://saucelabs.com/", "Expected URL does not match current URL '{url}'"