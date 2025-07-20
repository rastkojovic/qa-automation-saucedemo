class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
    
    def open(self):
        self.driver.get(self.URL)
        
    def get_title(self):
        return self.driver.title
    
    def is_element_visible(self, by, value):
        elements = self.driver.find_elements(by, value)
        return len(elements) > 0 and elements[0].is_displayed()
    
    def click(self, by, value):
        self.driver.find_element(by, value).click()
        
    def fill_field(self, by, value, data):
        self.driver.find_element(by, value).send_keys(data)