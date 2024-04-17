import pytest
from selenium.webdriver.common.by import By
import allure

from locators.reset_pass_locators import ResetPassPageLocators
from pages.forgot_pass_page import ForgotPassPage
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.reset_pass_page import ResetPassPage


class TestResetPassPage:
    @allure.title('Проверка клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @pytest.mark.parametrize("selected_driver", ['driver_chrome', 'driver_firefox'])
    def test_show_pass_field_true(self, request, selected_driver):
        driver = request.getfixturevalue(selected_driver)
        header_page = HeaderPage(driver)
        login_page = LoginPage(driver)
        forgot_pass_page = ForgotPassPage(driver)
        reset_pass_page = ResetPassPage(driver)

        random_email = 'kir_bel_66@yandex.ru'
        header_page.click_to_personal_account()
        login_page.click_to_restore_pass_button()
        forgot_pass_page.fill_and_to_click_o_restore_button(random_email)
        assert reset_pass_page.click_to_show_pass_field()
