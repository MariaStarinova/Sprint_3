from tests import data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import TestLocators

name, email, password = data.generate()
class TestRegistration:

    def test_login_account_button(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.LOGIN_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.HEADING_ON_LOG_IN_PAGE))

        driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(data.email)

        driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(data.password)

        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.ORDER_BUTTON))

        assert driver.find_element(*TestLocators.ORDER_BUTTON).text == "Оформить заказ"


    # def test_login_link(self, driver):
    #     driver.get("https://stellarburgers.nomoreparties.site/")
    #     driver.find_element(*TestLocators.LOGIN_LINK).click()
    #
    #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.HEADING_ON_LOG_IN_PAGE))
    #
    #     driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(email)
    #
    #     driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(password)
    #
    #     driver.find_element(*TestLocators.BUTTON_ENTER).click()
    #
    #     assert driver.find_element(*TestLocators.ORDER_BUTTON).text == "Оформить заказ"
    #
    #
    # def test_login_menu_registration(self, driver):
    #     driver.get("https://stellarburgers.nomoreparties.site/register")
    #     driver.find_element(*TestLocators.BUTTON_ENTER).click()
    #
    #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.HEADING_ON_LOG_IN_PAGE))
    #
    #     driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(email)
    #
    #     driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(password)
    #
    #     driver.find_element(*TestLocators.BUTTON_ENTER).click()
    #
    #     assert driver.find_element(*TestLocators.ORDER_BUTTON).text == "Оформить заказ"
    #
    #
    # def test_login_link_restore_password(self, driver):
    #     driver.get("https://stellarburgers.nomoreparties.site/login")






