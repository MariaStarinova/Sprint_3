import data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from faker import Faker

fake = Faker()
def generate():
    name = fake.name()
    email = fake.email()
    password = fake.password(length=6)
    return name, email, password

class TestRegistration:

    def test_registration_success(self, driver):
        name, email, password = generate()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.NAME_INPUT_REGISTRATION).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_INPUT_REGISTRATION).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_REGISTRATION).send_keys(password)
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.HEADING_ON_LOG_IN_PAGE))
        assert driver.find_element(*TestLocators.HEADING_ON_LOG_IN_PAGE).text == "Вход"

    def test_registration_password_lower_six_symbols(self, driver):
        name, email, password = generate()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.NAME_INPUT_REGISTRATION).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_INPUT_REGISTRATION).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_REGISTRATION).send_keys(password[:5])
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.PASSWORD_ERROR_REGISTRATION))
        assert driver.find_element(*TestLocators.PASSWORD_ERROR_REGISTRATION).text == "Некорректный пароль"
