from locators.login_page_locators import LoginPageLocators
from urls import Urls


class TestLoginPage:
    def test_open_login_page_from_header_true(self, header_page, personal_page):
        header_page.click_to_personal_account()
        assert LoginPageLocators.login_button_locator and personal_page.get_url() == Urls.login_url
