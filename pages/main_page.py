import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Клик на "Ингредиент"')
    def click_to_ingredient(self):
        self.click_on_element(MainPageLocators.bun_locator)

    @allure.step('Закрытие модального окна на крестик')
    def close_modal_window(self):
        self.wait_for_element(MainPageLocators.close_modal_window_button_locator).is_enabled()
        self.click_on_element(MainPageLocators.close_modal_window_button_locator)

    @allure.step('Добавление ингредиента для заказа')
    def adding_ingredient_for_order(self):
        self.move_element(MainPageLocators.bun_locator, MainPageLocators.buns_constructor_locator)

    @allure.step('Клик на кнопку "Оформить заказ"')
    def click_to_checkout_button(self):
        self.click_on_element(MainPageLocators.checkout_button_locator)
