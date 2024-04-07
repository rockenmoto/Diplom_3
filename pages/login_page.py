from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def click_to_login_button(self):
        self.click_on_element(LoginPageLocators.login_button_locator)
