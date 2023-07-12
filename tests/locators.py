from selenium.webdriver.common.by import By

class TestLocators:
    # Локаторы для проверки регистрации
    NAME_INPUT_REGISTRATION = By.XPATH,'.//label[text()="Имя"]/following-sibling::input'
    EMAIL_INPUT_REGISTRATION = By.XPATH,'.//label[text()="Email"]/following-sibling::input'
    PASSWORD_INPUT_REGISTRATION = By.XPATH, './/input[(@name="Пароль")]'
    REGISTER_BUTTON = By.XPATH, './/button[text()="Зарегистрироваться"]'
    PASSWORD_ERROR_REGISTRATION = By.XPATH, './/p[text()="Некорректный пароль"]'
    # Локаторы для проверки авторизации
    HEADING_ON_LOG_IN_PAGE = By.XPATH, './/h2[text()="Вход"]'
    BUTTON_ENTER = By.XPATH, './/button[text()="Войти"]'
    LOGIN_LINK = By.XPATH, './/p[text()="Личный Кабинет"]'
    LOGIN_ACCOUNT_BUTTON = By.XPATH, './/button[contains(text(),"Войти в аккаунт")]'
    PASSWORD_INPUT_LOGIN = By.XPATH, './/input[(@name="Пароль")]'
    EMAIL_INPUT_LOGIN = By.XPATH, './/label[text()="Email"]/following-sibling::input'
    LINK_RESTORE_PASSWORD = By.XPATH, './/button[text()="Восстановить пароль"]'
    ORDER_BUTTON = By.XPATH, './/button[text()="Оформить заказ"]'
    BUTTON_ENTER_FIELD = By.XPATH, './/*[text()="Войти"]'
    # Локаторы для проверки выхода из профиля
    LOGOUT_BUTTON = By.XPATH, './/button[text()="Выход"]'
    ACCOUNT_BUTTON = By.XPATH, './/p[text()="Личный Кабинет"]'
    # Локаторы для проверки переходов
    CONSTRUCTOR = By.XPATH, './/p[text()="Конструктор"]'
    LOGO = By.XPATH, './/a[@href="/"]'
    # Локаторы проверки переходов к разделам
    BUTTON_ROLLS = By.XPATH, './/div/div/*[text()="Булки"]'
    BUTTON_SAUCES = By.XPATH, './/div/div/*[text()="Соусы"]'
    BUTTON_TOPPINGS = By.XPATH, './/div/div/*[text()="Начинки"]'
    TEXT_ROLLS = By.XPATH, './/h2[text()="Булки"]'
    TEXT_SAUCES = By.XPATH, './/h2[text()="Соусы"]'
    TEXT_TOPPINGS = By.XPATH, './/h2[text()="Начинки"]'



