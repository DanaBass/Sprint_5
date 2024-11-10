from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

class TestSiteNavigation:
    def test_transition_personal_account(self, driver_logged_in_personal_account):
        assert driver_logged_in_personal_account.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_transition_to_the_constructor(self, driver_logged_in_personal_account):
        driver_logged_in_personal_account.find_element(*TestLocators.LOCATOR_CONSTRUCTOR).click()
        WebDriverWait(driver_logged_in_personal_account, 10).until(expected_conditions.element_to_be_clickable(TestLocators.LOCATOR_BUTTON_BURGER))

        finded_field = driver_logged_in_personal_account.find_element(*TestLocators.LOCATOR_BUTTON_BURGER)

        assert finded_field.text == 'Соберите бургер'

    def test_transition_to_the_logo(self, driver_logged_in_personal_account):
        driver_logged_in_personal_account.find_element(*TestLocators.LOCATOR_LOGO).click()
        WebDriverWait(driver_logged_in_personal_account, 10).until(expected_conditions.element_to_be_clickable(TestLocators.LOCATOR_BUTTON_BURGER))

        finded_field = driver_logged_in_personal_account.find_element(*TestLocators.LOCATOR_BUTTON_BURGER)

        assert finded_field.text == 'Соберите бургер'