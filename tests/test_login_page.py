import allure
import pytest

from pages.forgot_pass_page import ForgotPassPage
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from urls import Urls


class TestLoginPage:
    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    @pytest.mark.parametrize("selected_driver", ['driver_chrome', 'driver_firefox'])
    def test_open_login_page_from_header_true(self, request, selected_driver):
        driver = request.getfixturevalue(selected_driver)
        header_page = HeaderPage(driver)
        login_page = LoginPage(driver)

        header_page.click_to_personal_account()
        assert login_page.get_login_button_text() == 'Войти'
        assert login_page.get_url() == Urls.login_url

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @pytest.mark.parametrize("selected_driver", ['driver_chrome', 'driver_firefox'])
    def test_open_forgot_pass_page_true(self, request, selected_driver):
        driver = request.getfixturevalue(selected_driver)
        header_page = HeaderPage(driver)
        login_page = LoginPage(driver)
        forgot_pass_page = ForgotPassPage(driver)

        header_page.click_to_personal_account()
        login_page.click_to_restore_pass_button()
        assert forgot_pass_page.get_restore_button_text() == 'Восстановить'
        assert forgot_pass_page.get_url() == Urls.forgot_pass_url
