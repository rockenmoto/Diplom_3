import pytest

from locators.login_page_locators import LoginPageLocators
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.personal_page import PersonalPage
from urls import Urls
from user import User
import allure


class TestPersonalPage:
    user = User()
    user_data = []

    @classmethod
    def setup_method(cls):
        cls.user_data = cls.user.create_new_user()

    @allure.title('Проверка переход в раздел «История заказов»')
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

    @allure.title('Проверка выход из аккаунта')
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
        assert (personal_page.wait_for_element(LoginPageLocators.login_button_locator)
                and personal_page.get_url() == Urls.login_url)

    @classmethod
    def teardown_method(cls):
        cls.user.delete_user(cls.user_data[3])
