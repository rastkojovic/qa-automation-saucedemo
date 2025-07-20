import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    # Added to prevent test interferance  
    options = Options()
    prefs = {
        "profile.password_manager_leak_detection": False,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument('--disable-save-password-bubble')
    options.add_argument('--disable-features=PasswordLeakDetection,PasswordManagerLeakDetection')
    options.add_argument('--disable-infobars')
    options.add_argument('--incognito')

    
    driver_path = os.path.join(os.path.dirname(__file__), 'drivers', 'chromedriver.exe')
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()