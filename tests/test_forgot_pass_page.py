from locators.reset_pass_locators import ResetPassPageLocators
from user_data import UserData
from urls import Urls
import allure


class TestForgotPassPage:
    def test_fill_email_and_click_to_restore_button_true(self, header_page, login_page,
                                                         forgot_pass_page, reset_pass_page):
        header_page.click_to_personal_account()
        login_page.click_to_restore_pass_button()
        forgot_pass_page.fill_and_to_click_o_restore_button(UserData.email)
        assert reset_pass_page.wait_for_element(
            ResetPassPageLocators.save_button_locator) and reset_pass_page.get_url() == Urls.reset_pass_url
