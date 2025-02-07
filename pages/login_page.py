import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Perform logging with mail and password')
    def login(self, email, password):
        self.fill_in_field(LoginPageLocators.email_input_locator, email)
        self.fill_in_field(LoginPageLocators.pass_input_locator, password)
        self.click_to_login_button()

    @allure.step('Click on the button "Sign in"')
    def click_to_login_button(self):
        self.click_on_element(LoginPageLocators.login_button_locator)

    @allure.step('Click on the button "Restore"')
    def click_to_restore_pass_button(self):
        self.click_on_element(LoginPageLocators.restore_pass_link_locator)

    @allure.step('Get the name of the button "Sign in"')
    def get_login_button_text(self):
        return self.get_text_element(LoginPageLocators.login_button_locator)
