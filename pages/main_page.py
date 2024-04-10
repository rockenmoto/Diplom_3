from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def click_to_ingredient(self):
        self.click_on_element(MainPageLocators.bun_locator)

    def close_modal_window(self):
        self.click_on_element(MainPageLocators.close_modal_window_button)
