# Use Pytest using Page Object Model

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Test_Data.data import Subash_Data
from Test_Locators.locators import Subash_Locators
import pytest

class Test_Subash:

    #Booting method for running the Pytest test cases
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        yield
        
    def test_login(self, boot):
        self.driver.get(Subash_Data().url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=Subash_Locators().username_input_box).send_keys(Subash_Data().username)
        self.driver.find_element(by=By.NAME, value=Subash_Locators().password_input_box).send_keys(Subash_Data().password)
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().submit_button).click()
        print("The user is Ivalid Credentials")
        while(True):
            pass        
