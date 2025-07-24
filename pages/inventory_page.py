from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    
    URL = "https://www.saucedemo.com/inventory.html"
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def is_loaded(self):
        return self.driver.find_element(By.ID, "inventory_container")
    
    def get_product_container_by_name(self, product_name):
        product_names = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        for name in product_names:
            if name.text == product_name:
                return name.find_element(By.XPATH, "../../..")
        raise Exception(f"Product '{product_name}' not found")
    
    def add_to_cart(self, product_name):
        product_container = self.get_product_container_by_name(product_name)
        add_to_cart_button = product_container.find_element(By.CLASS_NAME, "btn_inventory")
        add_to_cart_button.click()
        
    def remove_from_cart(self, product_name):
        product_container = self.get_product_container_by_name(product_name)
        remove_from_cart_button = product_container.find_element(By.CLASS_NAME, "btn_inventory")
        remove_from_cart_button.click()
        
    def get_cart_count(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        return elements[0].text if elements else "0"
    
    def open_product_page(self, product_name):
        product_names = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
        
        for name in product_names:
            print(name.text)
            if name.text == product_name:
                name.find_element(By.XPATH, '..').click()
                return
            
        raise Exception(f"Product page '{product_name}' not found!")
    
    def open_cart_page(self):
        self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
        
    def get_cart_badge_num(self):
        cart_badge_element = self.driver.find_element(By.CSS_SELECTOR, "span.shopping_cart_badge")
        return cart_badge_element.text
        
    def open_burger_menu(self):
        burger_menu = self.driver.find_element(By.ID, "react-burger-menu-btn")
        burger_menu.click()
        
    def open_sorting_dropdown(self):
        sorting_dropdown = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        sorting_dropdown.click()
        
    def get_active_sorting_dropdown_option(self):
        active_sort_option_element = self.driver.find_element(By.CSS_SELECTOR, "span.active_option")
        return active_sort_option_element.text
        
    def get_inventory_item_names(self):
        inventory_item_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        inventory_item_names = [item.text for item in inventory_item_elements]
        return inventory_item_names
    
    def get_inventory_item_prices(self):
        inventory_item_price_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        inventory_item_prices = [float(item.text[1:]) for item in inventory_item_price_elements]
        return inventory_item_prices
    
    def open_social(self, social_name):
        social_element = self.driver.find_element(By.CSS_SELECTOR, f"a[data-test='social-{social_name.lower()}']")
        social_element.click()