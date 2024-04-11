from locators.login_page_locators import LoginPageLocators
from urls import Urls


class TestPersonalPage:
    def test_open_history_order_section_true(self, login, header_page, personal_page):
        header_page.click_to_personal_account()
        personal_page.click_on_history_order_section()
        assert personal_page.get_url() == Urls.order_history_url

    def test_logout_true(self, login, header_page, personal_page):
        header_page.click_to_personal_account()
        personal_page.click_to_logout_button()
        assert (personal_page.wait_for_element(LoginPageLocators.login_button_locator)
                and personal_page.get_url() == Urls.login_url)
