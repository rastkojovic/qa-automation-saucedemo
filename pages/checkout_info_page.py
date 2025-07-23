from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutInfoPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def send_data(self, field_id, data):
        data_field = self.driver.find_element(By.ID, field_id)
        data_field.send_keys(data)
        
    def fill_first_name(self, first_name):
        self.send_data("first-name", first_name)
    
    def fill_last_name(self, last_name):
        self.send_data("last-name", last_name)
    
    def fill_postal_code(self, postal_code):
        self.send_data("postal-code", postal_code)
    
    def continue_checkout(self):
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()