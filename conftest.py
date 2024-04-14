import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_page import PersonalPage
from pages.header_page import HeaderPage
from pages.forgot_pass_page import ForgotPassPage
from pages.reset_pass_page import ResetPassPage
from pages.order_feed_page import OrderFeedPage


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.maximize_window()
    yield driver
    driver.quit()


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
