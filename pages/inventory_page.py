from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    
    URL = "https://www.saucedemo.com/inventory.html"
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def is_loaded(self):
        return self.driver.find_element(By.ID, "inventory_container")
    
    def add_to_cart(self, by, value):
        self.driver.find_element(by, value).click()
        
    def remove_from_cart(self, by, value):
        self.driver.find_element(by, value).click()
        
    def get_cart_count(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        return elements[0].text if elements else "0"