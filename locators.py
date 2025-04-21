from selenium.webdriver.common.by import By


class Locators:
    # Локаторы для регистрации
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    NEW_ACCOUNT = (By.CSS_SELECTOR, "a[href='/register']")
    REG_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    NAME = By.XPATH,"//fieldset[1]//input[@type='text']"
    EMAIL = By.XPATH,"//fieldset[2]//input[@type='text']"
    PASSWORD = By.XPATH,"//fieldset[3]//input[@type='password']"
    REGISTER_BUTTON = By.XPATH, "//button[@class='auth-form__button']"

    REG_POPUP = (By.XPATH, "//p[@class='popup__status-message']")
    # Локаторы для изменения аватара
    PROFILE_IMAGE = (By.XPATH, "//div[@class='profile__image']")
    AVATAR_INPUT = (By.ID, "owner-avatar")
    UPDATE_AVATAR_BUTTON = (By.XPATH, "//form[@name='edit-avatar']/button[@class='button popup__button']")
    CARDS = (By.CLASS_NAME, "card__image")