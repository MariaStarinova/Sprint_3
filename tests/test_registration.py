from tests import data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import TestLocators


class TestRegistration:


    # Проверка успешной регистрации
    def test_registration_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.NAME_INPUT_REGISTRATION).send_keys(data.name)
        driver.find_element(*TestLocators.EMAIL_INPUT_REGISTRATION).send_keys(data.email)

        driver.find_element(*TestLocators.PASSWORD_INPUT_REGISTRATION).send_keys(data.password)

        driver.find_element(*TestLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.HEADING_ON_LOG_IN_PAGE))
        assert driver.find_element(*TestLocators.HEADING_ON_LOG_IN_PAGE).text == "Вход"


    # Проверка ошибки регистрации для некорректного пароля (меньше 6 символов)
    def test_registration_password_lower_six_symbols(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.NAME_INPUT_REGISTRATION).send_keys(data.name)
        driver.find_element(*TestLocators.EMAIL_INPUT_REGISTRATION).send_keys(data.email)

        driver.find_element(*TestLocators.PASSWORD_INPUT_REGISTRATION).send_keys(data.password[:5])

        driver.find_element(*TestLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.PASSWORD_ERROR_REGISTRATION))
        assert driver.find_element(*TestLocators.PASSWORD_ERROR_REGISTRATION).text == "Некорректный пароль"











