from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from selenium.webdriver.support import expected_conditions as EC

class TestLogout:
    def test_logout_of_your_personal_account(self, driver, user_data):
        driver.find_element(*TestLocators.ACCOUNT_LOGIN_LOCATOR).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.ACCOUNT_REGISTRATION_LOCATOR))

        driver.find_element(*TestLocators.LOCATOR_AUTHORIZATION_EMAIL).send_keys(user_data.login)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.LOCATOR_AUTHORIZATION_PASSWORD))

        driver.find_element(*TestLocators.LOCATOR_AUTHORIZATION_PASSWORD).send_keys(user_data.password)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.ACCOUNT_REGISTRATION_LOCATOR))

        driver.find_element(*TestLocators.LOCATOR_LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.LOCATOR_PLACE_AN_ORDER))

        driver.find_element(*TestLocators.LOCATOR_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))

        driver.find_element(*TestLocators.LOCATOR_BUTTON_EXIT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'