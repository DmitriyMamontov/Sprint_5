from selenium.webdriver.common.by import By


class Locators:

    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка "Войти в аккаунт"
    NEW_ACCOUNT = (By.CSS_SELECTOR, "a[href='/register']") # Кнопка "Создать аккаунт"
    REG_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input") # Поле ввода Имени
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input") # Поле ввода Email
    PASSWORD = (By.XPATH, "//input[@type='password']") # Поле ввода Пароля
    LOG_BUTTON = (By.XPATH, "//button[text()='Войти']") # Кнопка "Войти"
    NEW_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка "Новый заказ"

    REG_POPUP_ERROR_USER = (By.XPATH, "//p[text()='Такой пользователь уже существует']") # Сообщение что пользователь зарегистрирован
    REG_POPUP_ERROR_INCORRECT_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']") # Сообщение о неправильном пароле

    LOG_EMAIL = (By.NAME, "name") # Поле ввода email на экране для входа
    LOG_PASSWORD = (By.NAME, "Пароль") # Поле ввода пароля на экране для входа
    LOGIN_REG = (By.CSS_SELECTOR, "a[href='/login']") # Гиперссылка Войти на странице регистрации
    FORGOT_PASSWORD = (By.CSS_SELECTOR, "a[href='/forgot-password']") # Кнопка "Забыл пароль"

    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']") # Кнопка "Личный кабинет"
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']") # Кнопка "Сохранить" в личном кабинете
    HISTORY_ORDERS = (By.CSS_SELECTOR, "a[href='/account/order-history']") # Вкладка История заказов

    CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']") # Кнопка "Конструктор"
    CONSTRUCTOR_MENU = (By.CLASS_NAME, "App_componentContainer__2JC2W") # Меню Конструктора
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # Лого Stellar Burger
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']") # Кнопка Выйти из аккаунта

    BUTTON_TOPPINGS = (By.XPATH, "//span[text()='Начинки']/parent::div") # Вкладка "Начинки"
    BUTTON_BUNS = (By.XPATH, "//span[text()='Булки']/parent::div") # Вкладка "Булки"
    BUTTON_SAUCES = (By.XPATH, "//span[text()='Соусы']/parent::div") # Вкладка "Соусы"
    ACTIVE_SECTION = (By.CSS_SELECTOR, "div.tab_tab_type_current__2BEPc") # Индикатор активной вкладки

