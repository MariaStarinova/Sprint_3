from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from data import valid_email, valid_password

class TestLogin:

    def test_login_account_button(self, driver):
        driver.find_element(*TestLocators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.HEADING_ON_LOG_IN_PAGE))
        driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(valid_email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(valid_password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert driver.find_element(*TestLocators.ORDER_BUTTON).text == "Оформить заказ"

    def test_login_link(self, driver):
        driver.find_element(*TestLocators.LOGIN_LINK).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.HEADING_ON_LOG_IN_PAGE))
        driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(valid_email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(valid_password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert driver.find_element(*TestLocators.ORDER_BUTTON).text == "Оформить заказ"

    def test_login_menu_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.BUTTON_ENTER_FIELD).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.HEADING_ON_LOG_IN_PAGE))
        driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(valid_email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(valid_password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert driver.find_element(*TestLocators.ORDER_BUTTON).text == "Оформить заказ"

    def test_login_link_restore_password(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(*TestLocators.BUTTON_ENTER_FIELD).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.HEADING_ON_LOG_IN_PAGE))
        driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(valid_email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(valid_password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert driver.find_element(*TestLocators.ORDER_BUTTON).text == "Оформить заказ"
