from pages.base_page import BasePage
from locators.personal_page_locators import PersonalPageLocators


class PersonalPage(BasePage):

    def click_to_login_button(self):
        self.click_on_element(PersonalPageLocators.login_button_locator)

    def click_on_section(self, locator_section):
        self.click_on_element(locator_section)
