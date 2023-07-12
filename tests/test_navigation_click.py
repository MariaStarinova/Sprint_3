from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import TestLocators
from data import valid_email, valid_password

class TestRegistration:

    #Проверка перехода по клику на «Личный кабинет»--failed
    def test_navigation_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")

        driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(valid_email)

        driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(valid_password)

        driver.find_element(*TestLocators.BUTTON_ENTER).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.ACCOUNT_BUTTON)).click()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"



    # Проверка перехода из личного кабинета по клику на «Конструктор»
    def test_navigation_personal_account_click_constructor(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")

        driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(valid_email)

        driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(valid_password)

        driver.find_element(*TestLocators.BUTTON_ENTER).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR)).click()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

   # Проверка перехода по клику на логотип Stellar Burgers
    def test_navigation_personal_account_click_logo(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")

        driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(valid_email)

        driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(valid_password)

        driver.find_element(*TestLocators.BUTTON_ENTER).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.LOGO)).click()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"