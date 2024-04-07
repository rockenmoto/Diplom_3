from locators.forgot_pass_page_locators import ForgotPassPageLocators
from urls import Urls


class TestForgotPassPage:
    def test_open_restore_pass_page_true(self, header_page, login_page, forgot_pass_page):
        header_page.click_to_personal_account()
        login_page.click_to_restore_pass_button()
        assert forgot_pass_page.wait_for_element(
            ForgotPassPageLocators.restore_button_locator) and forgot_pass_page.get_url() == Urls.forgot_pass_url
