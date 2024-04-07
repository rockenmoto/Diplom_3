from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.reset_pass_locators import ResetPassPageLocators


class ResetPassPage(BasePage):
    def click_to_show_pass_field(self):
        self.click_on_element(ResetPassPageLocators.eye_icon)
        pass_field_active = True
        pass_field = self.driver.find_element(By.XPATH, ResetPassPageLocators.pass_input).get_attribute('class')
        if 'input_status_active' not in pass_field:
            pass_field_active = False
        return pass_field_active
