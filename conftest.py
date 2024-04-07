import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_page import PersonalPage
from pages.header_page import HeaderPage
from locators.login_page_locators import LoginPageLocators


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login(driver, header_page, login_page):
    USER_LOGIN_DATA = {
        'email': 'kirill_belov_666@yandex.ru',
        'password': 'yandexPractikumRulit'
    }

    header_page.click_to_personal_account()
    login_page.fill_in_field(LoginPageLocators.email_input_locator, USER_LOGIN_DATA['email'])
    login_page.fill_in_field(LoginPageLocators.pass_input_locator, USER_LOGIN_DATA['password'])
    login_page.click_to_login_button()


@pytest.fixture(scope="function")
def header_page(driver):
    return HeaderPage(driver)


@pytest.fixture(scope="function")
def main_page(driver):
    return MainPage(driver)


@pytest.fixture(scope="function")
def personal_page(driver):
    return PersonalPage(driver)


@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver)
