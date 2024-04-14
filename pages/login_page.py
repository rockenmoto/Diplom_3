import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Выполнение логирования с почтой и паролем')
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
