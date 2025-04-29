from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import *
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestNavigationSections:

    def test_switch_to_sauces_section(self, driver):
        sauces_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.BUTTON_SAUCES)
        )
        sauces_tab.click()

        active_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ACTIVE_SECTION)
        )
        assert active_tab.text == Sections.SAUCES
        assert Classes.ACTIVE_TAB in sauces_tab.get_attribute("class")

    def test_switch_to_toppings_section(self, driver):
        toppings_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.BUTTON_TOPPINGS)
        )
        toppings_tab.click()
        active_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ACTIVE_SECTION)
        )
        assert active_tab.text == Sections.TOPPINGS
        assert Classes.ACTIVE_TAB in toppings_tab.get_attribute("class")

    def test_switch_to_buns_section(self, driver):
        toppings_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.BUTTON_TOPPINGS)
        )
        toppings_tab.click()

        buns_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.BUTTON_BUNS)
        )
        buns_tab.click()

        active_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ACTIVE_SECTION)
        )
        assert active_tab.text == Sections.BUNS
        assert Classes.ACTIVE_TAB in buns_tab.get_attribute("class")