from pages.base_page import BasePage
from locators.forgot_pass_page_locators import ForgotPassPageLocators
import allure


class ForgotPassPage(BasePage):
    @allure.step('Заполняем емайл и кликаем по кнопку "Восстановить"')
    def fill_and_to_click_o_restore_button(self, email):
        self.fill_in_field(ForgotPassPageLocators.email_input_locator, email)
        self.click_on_element(ForgotPassPageLocators.restore_button_locator)
