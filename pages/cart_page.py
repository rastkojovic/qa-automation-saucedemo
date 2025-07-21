from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    
    URL = "https://www.saucedemo.com/cart.html"
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def get_cart_items(self):
        cart_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return cart_items