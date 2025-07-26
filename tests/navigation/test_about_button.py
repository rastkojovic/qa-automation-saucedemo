from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_data import SAUCELABS_URL

def test_about_button(driver, login_standard_user):
    """
    Test Case: TC014 - About Button Test
    """
    
    inventory_page = InventoryPage(driver)
    inventory_page.open_burger_menu()
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, "about_sidebar_link")))
    
    about_button = driver.find_element(By.ID, "about_sidebar_link")
    about_button.click()
    
    url = driver.current_url
    assert url == SAUCELABS_URL, "Expected URL does not match current URL '{url}'"