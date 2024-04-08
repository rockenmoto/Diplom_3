from pages.base_page import BasePage
from locators.reset_pass_locators import ResetPassPageLocators
import allure


class ResetPassPage(BasePage):
    @allure.step('Клик по иконке "Глаз"')
    def click_to_show_pass_field(self):
        self.click_on_element(ResetPassPageLocators.eye_icon)
        pass_field_active = True
        pass_field = self.get_class_attribute(ResetPassPageLocators.pass_input)

        if 'input_status_active' not in pass_field:
            pass_field_active = False
        return pass_field_active
