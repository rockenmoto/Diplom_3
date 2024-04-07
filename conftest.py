import pytest
from selenium import webdriver

from pages.main_page import MainPage
from pages.personal_page import PersonalPage
from pages.header_page import HeaderPage
from pages.order_history_page import OrderHistoryPage
from locators.personal_page_locators import PersonalPageLocators


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login(driver, header_page, personal_page):
    USER_LOGIN_DATA = {
        'email': 'kirill_belov_666@yandex.ru',
        'password': 'yandexPractikumRulit'
    }

    header_page.click_to_personal_account()
    personal_page.fill_in_field(PersonalPageLocators.email_input_locator, USER_LOGIN_DATA['email'])
    personal_page.fill_in_field(PersonalPageLocators.password_input_locator, USER_LOGIN_DATA['password'])
    personal_page.click_to_login_button()


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
def order_history_page(driver):
    return OrderHistoryPage(driver)
