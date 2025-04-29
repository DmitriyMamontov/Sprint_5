from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestRegistrationWithNewCredentials:

    def test_success_registration_new_account(self, driver, registration):
        email, password, name = generate_registration_data()
        driver = registration
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 10).until(
                EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
            )
        assert driver.current_url == main_site + 'login'

class TestRegistrationAccountPreviouslyCreated:

    def test_error_registration_previously_created_account(self, driver, registration):
        driver = registration
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.NAME).send_keys(Credentials.name)
        driver.find_element(*Locators.REG_BUTTON).click()
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.REG_POPUP_ERROR_USER)
        )

class TestRegistrationWithEmptyField:

    def test_stop_registration_account_empty_email(self, driver, registration):
        email, password, name = generate_registration_data()
        driver = registration
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.REG_BUTTON)
        )

    def test_stop_registration_account_empty_name(self, driver, registration):
        email, password, name = generate_registration_data()
        driver = registration
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.REG_BUTTON)
        )

    def test_stop_registration_account_empty_password(self, driver, registration):
        email, password, name = generate_registration_data()
        driver = registration
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_BUTTON).click()
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.REG_BUTTON)
        )

class TestRegistrationWithIncorrectPassword:

    def test_error_registration_account_incorrect_password(self, driver, registration):
        email, password, name = generate_registration_data()
        driver = registration
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys('123')
        driver.find_element(*Locators.REG_BUTTON).click()
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.REG_POPUP_ERROR_INCORRECT_PASSWORD)
        )