import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import UserData
from helpers import RandomRegistrationGenerator
from locators import TestLocators

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()

@pytest.fixture()
def user_data():
    return UserData('dana_panfilova_15_478@yandex.ru', 'Potolok15')

@pytest.fixture()
def random_user_data():
    name = RandomRegistrationGenerator.generate_random_name()
    email = RandomRegistrationGenerator.generate_random_email()
    password = RandomRegistrationGenerator.generate_password_random()
    return UserData(email, password, name)

@pytest.fixture()
def random_user_data_with_incorrect_password():
    name = RandomRegistrationGenerator.generate_random_name()
    email = RandomRegistrationGenerator.generate_random_email()
    incorrect_password = RandomRegistrationGenerator.generate_incorrect_password()
    return UserData(email, incorrect_password, name)

@pytest.fixture()
def driver_logged_in_personal_account(driver, user_data):
    driver.find_element(*TestLocators.LOCATOR_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.ACCOUNT_REGISTRATION_LOCATOR))

    driver.find_element(*TestLocators.LOCATOR_AUTHORIZATION_EMAIL).send_keys(user_data.login)
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.LOCATOR_AUTHORIZATION_PASSWORD))

    driver.find_element(*TestLocators.LOCATOR_AUTHORIZATION_PASSWORD).send_keys(user_data.password)
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.ACCOUNT_REGISTRATION_LOCATOR))

    driver.find_element(*TestLocators.LOCATOR_LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.LOCATOR_PLACE_AN_ORDER))

    driver.find_element(*TestLocators.LOCATOR_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 10).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))

    return driver

@pytest.fixture()
def driver_prepared_to_register_without_password(driver, user_data):
    driver.find_element(*TestLocators.ACCOUNT_LOGIN_LOCATOR).click()
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.ACCOUNT_REGISTRATION_LOCATOR))

    driver.find_element(*TestLocators.ACCOUNT_REGISTRATION_LOCATOR).click()
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.NAME_REGISTRATION))

    driver.find_element(*TestLocators.NAME_REGISTRATION).send_keys(user_data.name)
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.EMAIL_REGISTRATION))

    driver.find_element(*TestLocators.EMAIL_REGISTRATION).send_keys(user_data.login)
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.PASSWORD_REGISTRATION))