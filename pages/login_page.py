from pages.base_page import BasePage
from pages.header_page import HeaderPage
from locators.login_page_locators import LoginPageLocators
import allure

from user_data import UserData


class LoginPage(BasePage):
    def login(self, email, password):
        self.fill_in_field(LoginPageLocators.email_input_locator, email)
        self.fill_in_field(LoginPageLocators.pass_input_locator, password)
        self.click_to_login_button()

    @allure.step('Клик по кнопке "Войти"')
    def click_to_login_button(self):
        self.click_on_element(LoginPageLocators.login_button_locator)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_to_restore_pass_button(self):
        self.click_on_element(LoginPageLocators.restore_pass_link_locator)
