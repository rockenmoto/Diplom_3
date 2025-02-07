from pages.base_page import BasePage
from locators.header_page_locators import HeaderPageLocators
import allure


class HeaderPage(BasePage):
    @allure.step('Click on "Personal cabinet"')
    def click_to_personal_account(self):
        self.click_on_element(HeaderPageLocators.personal_account_locator)

    @allure.step('Click on "Order feed"')
    def click_to_order_feed(self):
        self.click_on_element(HeaderPageLocators.order_feed_locator)

    @allure.step('Click on "Constructor"')
    def click_to_constructor(self):
        self.click_on_element(HeaderPageLocators.constructor_locator)

    @allure.step('Click on the main logo "Stellar Burgers"')
    def click_to_main_logo(self):
        self.click_on_element(HeaderPageLocators.main_logo_locator)
