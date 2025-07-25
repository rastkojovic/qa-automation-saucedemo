from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from test_data import CART_PAGE_URL

class CartPage(BasePage):
    
    URL = CART_PAGE_URL
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def get_cart_items(self):
        cart_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return cart_items
    
    def remove_from_cart(self, item_name):
        cart_item_elements = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        
        for cart_item in cart_item_elements:
            cart_item_name = cart_item.find_element(By.CLASS_NAME, "inventory_item_name").text
            
            if cart_item_name == item_name:
                cart_item_button = cart_item.find_element(By.CLASS_NAME, "cart_button")
                cart_item_button.click()
                return
    
    def checkout(self):
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()
        