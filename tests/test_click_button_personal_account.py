from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestNavigationButtonPersonalAccount:

    def test_navigation_click_on_button_personal_account(self, driver, login):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        login()
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.HISTORY_ORDERS)
        )
        driver.quit()