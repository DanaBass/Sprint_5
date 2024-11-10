from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestLocators


class TestAuthorization:
    def test_registration_successful (self, driver, random_user_data):
        self.register(driver, random_user_data)

        driver.find_element(*TestLocators.PASSWORD_REGISTRATION).send_keys(random_user_data.password)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.ACCOUNT_REGISTER))

        driver.find_element(*TestLocators.ACCOUNT_REGISTER).click()
        WebDriverWait(driver, 10).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_registration_incorrect_password(self, driver, random_user_data_with_incorrect_password):
        self.register(driver, random_user_data_with_incorrect_password)

        driver.find_element(*TestLocators.ACCOUNT_REGISTER).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.LOCATOR_INCORRECT_PASSWORD))

        finded_field = driver.find_element(*TestLocators.LOCATOR_INCORRECT_PASSWORD)

        assert finded_field.text == "Некорректный пароль"

    @staticmethod
    def register(driver, user_data):
        driver.find_element(*TestLocators.ACCOUNT_LOGIN_LOCATOR).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.ACCOUNT_REGISTRATION_LOCATOR))

        driver.find_element(*TestLocators.ACCOUNT_REGISTRATION_LOCATOR).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.NAME_REGISTRATION))

        driver.find_element(*TestLocators.NAME_REGISTRATION).send_keys(user_data.name)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.EMAIL_REGISTRATION))

        #
        driver.find_element(*TestLocators.EMAIL_REGISTRATION).send_keys(user_data.login)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.PASSWORD_REGISTRATION))

        driver.find_element(*TestLocators.PASSWORD_REGISTRATION).send_keys(user_data.password)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.ACCOUNT_REGISTER))