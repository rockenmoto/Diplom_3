from pages.base_page import BasePage
from locators.header_page_locators import HeaderPageLocators
import allure


class HeaderPage(BasePage):
    @allure.step('Клик на "Личный кабинет"')
    def click_to_personal_account(self):
        self.click_on_element(HeaderPageLocators.personal_account_locator)

    @allure.step('Клик на "Лента заказов"')
    def click_to_order_feed(self):
        self.click_on_element(HeaderPageLocators.order_feed_locator)

    @allure.step('Клик на "Конструктор"')
    def click_to_constructor(self):
        self.click_on_element(HeaderPageLocators.constructor_locator)
