from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
import allure


class LoginPage(BasePage):
    @allure.step('Клик по кнопке "Войти"')
    def click_to_login_button(self):
        self.click_on_element(LoginPageLocators.login_button_locator)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_to_restore_pass_button(self):
        self.click_on_element(LoginPageLocators.restore_pass_locator)
