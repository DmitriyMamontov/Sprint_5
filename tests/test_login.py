from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestLoginWithRegisteredEmail:

    def test_success_login(self,driver, login):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        login()
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.NEW_ORDER_BUTTON)
        )
        driver.quit()

    def test_success_login_via_personal_account_button(self, driver, login):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        login()
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.NEW_ORDER_BUTTON)
        )
        driver.quit()

    def test_success_login_via_registration_button(self, driver, login):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.NEW_ACCOUNT).click()
        driver.find_element(*Locators.LOGIN_REG).click()
        login()
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.NEW_ORDER_BUTTON)
        )
        driver.quit()

    def test_success_login_via_forgot_password_button(self, driver, login):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.FORGOT_PASSWORD).click()
        driver.find_element(*Locators.LOGIN_REG).click()
        login()
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.NEW_ORDER_BUTTON)
        )
        driver.quit()
