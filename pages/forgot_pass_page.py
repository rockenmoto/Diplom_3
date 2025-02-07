from pages.base_page import BasePage
from locators.forgot_pass_page_locators import ForgotPassPageLocators
import allure


class ForgotPassPage(BasePage):
    @allure.step('Fill in your e-mail address and click on the button "Restore"')
    def fill_and_to_click_o_restore_button(self, email):
        self.fill_in_field(ForgotPassPageLocators.email_input_locator, email)
        self.click_on_element(ForgotPassPageLocators.restore_button_locator)

    @allure.step('Get the name of the button "Restore"')
    def get_restore_button_text(self):
        return self.get_text_element(ForgotPassPageLocators.restore_button_locator)
