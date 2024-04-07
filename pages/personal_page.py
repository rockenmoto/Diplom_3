from pages.base_page import BasePage
from locators.personal_page_locators import PersonalPageLocators


class PersonalPage(BasePage):

    def click_on_history_order_section(self):
        self.click_on_element(PersonalPageLocators.order_history_locator)

    def click_to_logout_button(self):
        self.click_on_element(PersonalPageLocators.logout_button_locator)
