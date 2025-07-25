from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from test_data import SAUCEDEMO_URL

class LoginPage(BasePage):
    
    URL = SAUCEDEMO_URL
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def login(self, username, password):    
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        
    def login_standard_user(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()