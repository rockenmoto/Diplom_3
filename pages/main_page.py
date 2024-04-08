from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def click_to_ingredient(self):
        self.click_on_element(MainPageLocators.first_bun_locator)
