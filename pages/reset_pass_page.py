from pages.base_page import BasePage
from locators.reset_pass_locators import ResetPassPageLocators
import allure


class ResetPassPage(BasePage):
    @allure.step('Click on the icon "Eye"')
    def click_to_show_pass_field(self):
        self.click_on_element(ResetPassPageLocators.eye_icon_locator)
        pass_field_active = True
        pass_field = self.get_class_attribute(ResetPassPageLocators.pass_input_locator)

        if 'input_status_active' not in pass_field:
            pass_field_active = False
        return pass_field_active

    @allure.step('Get the name of the button "Save"')
    def get_save_button_text(self):
        return self.get_text_element(ResetPassPageLocators.save_button_locator)
