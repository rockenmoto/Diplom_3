import allure
import pytest

from locators.reset_pass_locators import ResetPassPageLocators
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.forgot_pass_page import ForgotPassPage
from pages.reset_pass_page import ResetPassPage
from urls import Urls
from user import User


class TestForgotPassPage:
    user = User()
    user_data = []

    @classmethod
    def setup_class(cls):
        cls.user_data = cls.user.create_new_user()

    @allure.title('Проверка ввод почты и клик по кнопке «Восстановить»')
    @pytest.mark.parametrize("selected_driver", ['driver_chrome', 'driver_firefox'])
    def test_fill_email_and_click_to_restore_button_true(self, request, selected_driver):
        driver = request.getfixturevalue(selected_driver)
        header_page = HeaderPage(driver)
        login_page = LoginPage(driver)
        forgot_pass_page = ForgotPassPage(driver)
        reset_pass_page = ResetPassPage(driver)

        header_page.click_to_personal_account()
        login_page.click_to_restore_pass_button()
        forgot_pass_page.fill_and_to_click_o_restore_button(self.user_data[0])
        assert reset_pass_page.wait_for_element(
            ResetPassPageLocators.save_button_locator) and reset_pass_page.get_url() == Urls.reset_pass_url

    @classmethod
    def teardown_class(cls):
        cls.user.delete_user(cls.user_data[3])
