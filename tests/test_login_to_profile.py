from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


class TestLoginToProfile:
    def test_login_button_home_page(self, driver, user_data):
        driver.find_element(*TestLocators.ACCOUNT_LOGIN_LOCATOR).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.ACCOUNT_REGISTRATION_LOCATOR))

        finded_field = self.login_to_account(driver, user_data)

        assert finded_field.text == 'Оформить заказ'

    def test_login_personal_account(self, driver, user_data):
        driver.find_element(*TestLocators.LOCATOR_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.ACCOUNT_REGISTRATION_LOCATOR))

        finded_field = self.login_to_account(driver, user_data)

        assert finded_field.text == 'Оформить заказ'

    def test_login_registration_form(self, user_data, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')

        driver.find_element(*TestLocators.LOCATOR_LOGIN).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.ACCOUNT_REGISTRATION_LOCATOR))

        finded_field = self.login_to_account(driver, user_data)

        assert finded_field.text == 'Оформить заказ'

    def test_login_password_recovery_form(self, driver, user_data):
        driver.get('https://stellarburgers.nomoreparties.site/login')

        driver.find_element(*TestLocators.LOCATOR_RESTORE_PASSWORD).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.LOCATOR_LOGIN_RESTORE))

        driver.find_element(*TestLocators.LOCATOR_LOGIN_RESTORE).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.ACCOUNT_REGISTRATION_LOCATOR))

        finded_field = self.login_to_account(driver, user_data)

        assert finded_field.text == 'Оформить заказ'

    @staticmethod
    def login_to_account(driver, user_data):
        driver.find_element(*TestLocators.LOCATOR_AUTHORIZATION_EMAIL).send_keys(user_data.login)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.LOCATOR_AUTHORIZATION_PASSWORD))

        driver.find_element(*TestLocators.LOCATOR_AUTHORIZATION_PASSWORD).send_keys(user_data.password)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.ACCOUNT_REGISTRATION_LOCATOR))

        driver.find_element(*TestLocators.LOCATOR_LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.LOCATOR_PLACE_AN_ORDER))

        finded_place_an_order_field = driver.find_element(*TestLocators.LOCATOR_PLACE_AN_ORDER)

        return finded_place_an_order_field
