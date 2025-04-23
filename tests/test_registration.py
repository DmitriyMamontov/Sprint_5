from locators import Locators
from curl import *

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get(main_site)

driver.find_element(*Locators.LOGIN_BUTTON).click()
driver.find_element(*Locators.NEW_ACCOUNT).click()
driver.find_element(*Locators.NAME).send_keys("Dmitry")
driver.find_element(*Locators.EMAIL).send_keys("q11w33366666666qwqw@ya.ru")
driver.find_element(*Locators.PASSWORD).send_keys("123456")
driver.find_element(*Locators.REG_BUTTON).click()
WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )
current_url = driver.current_url
assert driver.current_url == main_site + 'login'
driver.quit()




