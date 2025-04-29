from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestNavigationToConstructor:

    def test_navigation_click_on_button_constructor(self, driver, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.EXIT_BUTTON).click()
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.CONSTRUCTOR_MENU)
        )
