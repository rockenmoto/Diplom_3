import allure
import pytest

from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.personal_page import PersonalPage
from urls import Urls
from user import User


class TestPersonalPage:
    user = User()
    user_data = []

    @classmethod
    def setup_method(cls):
        cls.user_data = cls.user.create_new_user()

    @allure.title('Check transition to the “Order History” section')
    @pytest.mark.parametrize("selected_driver", ['driver_chrome', 'driver_firefox'])
    def test_open_history_order_section_true(self, request, selected_driver):
        driver = request.getfixturevalue(selected_driver)
        header_page = HeaderPage(driver)
        login_page = LoginPage(driver)
        personal_page = PersonalPage(driver)

        header_page.click_to_personal_account()
        login_page.login(self.user_data[0], self.user_data[1])
        header_page.click_to_personal_account()
        personal_page.click_on_history_order_section()
        assert personal_page.get_url() == Urls.order_history_url

    @allure.title('Checking account logout')
    @pytest.mark.parametrize("selected_driver", ['driver_chrome', 'driver_firefox'])
    def test_logout_true(self, request, selected_driver):
        driver = request.getfixturevalue(selected_driver)
        header_page = HeaderPage(driver)
        login_page = LoginPage(driver)
        personal_page = PersonalPage(driver)

        header_page.click_to_personal_account()
        login_page.login(self.user_data[0], self.user_data[1])
        header_page.click_to_personal_account()
        personal_page.click_to_logout_button()
        assert login_page.get_login_button_text() == 'Войти'
        assert login_page.get_url() == Urls.login_url

    @classmethod
    def teardown_method(cls):
        cls.user.delete_user(cls.user_data[3])
