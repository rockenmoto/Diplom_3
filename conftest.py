import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_page import PersonalPage
from pages.header_page import HeaderPage
from pages.forgot_pass_page import ForgotPassPage
from pages.reset_pass_page import ResetPassPage
from pages.order_feed_page import OrderFeedPage
from locators.login_page_locators import LoginPageLocators
from user_data import UserData


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login(header_page, login_page):
    header_page.click_to_personal_account()
    login_page.fill_in_field(LoginPageLocators.email_input_locator, UserData.email)
    login_page.fill_in_field(LoginPageLocators.pass_input_locator, UserData.password)
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


@pytest.fixture(scope="function")
def forgot_pass_page(driver):
    return ForgotPassPage(driver)


@pytest.fixture(scope="function")
def reset_pass_page(driver):
    return ResetPassPage(driver)


@pytest.fixture(scope="function")
def order_feed_page(driver):
    return OrderFeedPage(driver)

@pytest.fixture(scope="function")
def ordering_burger(driver):

    return OrderFeedPage(driver)
