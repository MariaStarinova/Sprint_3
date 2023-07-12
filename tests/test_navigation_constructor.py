from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators


class TestRegistration:

    # Проверка перехода к разделу «Булки»
    def test_navigation_list_of_rolls(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.BUTTON_ROLLS)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.TEXT_ROLLS))

        assert driver.find_element(*TestLocators.TEXT_ROLLS).text == "Булки"


     # Проверка перехода к разделу «Соусы»
    def test_navigation_list_of_sauces(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.BUTTON_SAUCES).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.TEXT_SAUCES))

        assert driver.find_element(*TestLocators.TEXT_SAUCES).text == "Соусы"


    # Проверка перехода к разделу «Начинки»
    def test_navigation_list_of_toppings(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.BUTTON_TOPPINGS).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.TEXT_TOPPINGS))

        assert driver.find_element(*TestLocators.TEXT_TOPPINGS).text == "Начинки"