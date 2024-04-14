from selenium.webdriver.common.by import By

from locators.reset_pass_locators import ResetPassPageLocators
from user_data import UserData


class TestResetPassPage:
    @allure.title('Проверка клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_show_pass_field_true(self, reset_pass_page, header_page, login_page, forgot_pass_page):
        header_page.click_to_personal_account()
        login_page.click_to_restore_pass_button()
        forgot_pass_page.fill_and_to_click_o_restore_button(UserData.email)
        assert reset_pass_page.click_to_show_pass_field()
