from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import TestLocators
from data import valid_email, valid_password

class TestRegistration:

    # Проверка выхода по кнопке «Выйти» в личном кабинете