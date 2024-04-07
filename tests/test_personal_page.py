from urls import Urls
from locators.personal_page_locators import PersonalPageLocators
from locators.order_history_page_locators import OrderHistoryPageLocators


class TestPersonalPage:
    def test_open_login_page_from_header_true(self, header_page, personal_page):
        header_page.click_to_personal_account()
        assert PersonalPageLocators.login_button_locator and personal_page.get_url() == Urls.login_url

    def test_login_from_sign_in_button_true(self, login, header_page, personal_page, order_history_page):
        header_page.click_to_personal_account()
        personal_page.click_on_section(OrderHistoryPageLocators.order_history_locator)
        assert order_history_page.get_url() == Urls.order_history_url

    def test_logout_true(self, login, header_page, personal_page):
        header_page.click_to_personal_account()
        personal_page.click_on_section(PersonalPageLocators.logout_button_locator)
        assert personal_page.wait_for_element(
            PersonalPageLocators.login_button_locator) and personal_page.get_url() == Urls.login_url
