from locators.forgot_pass_page_locators import ForgotPassPageLocators
from locators.login_page_locators import LoginPageLocators
from urls import Urls


class TestLoginPage:
    def test_open_login_page_from_header_true(self, header_page, personal_page):
        header_page.click_to_personal_account()
        assert LoginPageLocators.login_button_locator and personal_page.get_url() == Urls.login_url

    def test_open_forgot_pass_page_true(self, header_page, login_page, forgot_pass_page):
        header_page.click_to_personal_account()
        login_page.click_to_restore_pass_button()
        assert forgot_pass_page.wait_for_element(
            ForgotPassPageLocators.restore_button_locator) and forgot_pass_page.get_url() == Urls.forgot_pass_url
