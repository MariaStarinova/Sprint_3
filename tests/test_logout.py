from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import TestLocators
from data import valid_email, valid_password

class TestRegistration:

    # Проверка выхода по кнопке «Выйти» в личном кабинете
    def test_logout_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")

        driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(valid_email)

        driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(valid_password)

        driver.find_element(*TestLocators.BUTTON_ENTER).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.LOGOUT_BUTTON)).click()

        driver.find_element(*TestLocators.ACCOUNT_BUTTON).click()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"




