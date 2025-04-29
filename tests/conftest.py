import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from curl import *

from curl import *
from data import Credentials
from locators import Locators
@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.binary_location = r"C:\Users\USER\AppData\Local\Google\Chrome\Application\chrome.exe"
    options.add_argument("--window-size=1200,600")
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    driver.get(main_site)
    yield driver

    driver.quit()

@pytest.fixture
def registration(driver):
    """
    Фикстура для регистрации пользователя.
    """
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(*Locators.NEW_ACCOUNT).click()

    return driver

@pytest.fixture
def login(driver):
    """
    Фикстура только для выполнения авторизации (без перехода на страницу входа)
    """
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(*Locators.LOG_EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.LOG_PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.LOG_BUTTON).click()

    return driver