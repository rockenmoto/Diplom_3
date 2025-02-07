from pages.base_page import BasePage
from locators.personal_page_locators import PersonalPageLocators
import allure


class PersonalPage(BasePage):
    @allure.step('Click on a section "Order history"')
    def click_on_history_order_section(self):
        self.click_on_element(PersonalPageLocators.order_history_locator)

    @allure.step('Click on the button "Exit"')
    def click_to_logout_button(self):
        self.click_on_element(PersonalPageLocators.logout_button_locator)

    @allure.step('Receiving an order number')
    def get_order_id(self):
        return self.get_text_element(PersonalPageLocators.last_cell_order_id_locator)
