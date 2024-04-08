from pages.base_page import BasePage
from locators.header_page_locators import HeaderPageLocators
import allure


class HeaderPage(BasePage):
    @allure.step('Заполняем емайл и кликаем по кнопку "Восстановить"')
    def click_to_personal_account(self):
        self.click_on_element(HeaderPageLocators.personal_account_locator)
