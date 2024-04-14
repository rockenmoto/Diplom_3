from locators.reset_pass_locators import ResetPassPageLocators
from urls import Urls
from user import User
import allure


class TestForgotPassPage:
    user = User()
    user_data = []

    @classmethod
    def setup_class(cls):
        cls.user_data = cls.user.create_new_user()

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_fill_email_and_click_to_restore_button_true(self, header_page, login_page,
                                                         forgot_pass_page, reset_pass_page):
        header_page.click_to_personal_account()
        login_page.click_to_restore_pass_button()
        forgot_pass_page.fill_and_to_click_o_restore_button(self.user_data[0])
        assert reset_pass_page.wait_for_element(
            ResetPassPageLocators.save_button_locator) and reset_pass_page.get_url() == Urls.reset_pass_url

    @classmethod
    def teardown_class(cls):
        cls.user.delete_user(cls.user_data[3])
