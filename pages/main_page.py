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

    @allure.step('Открылось модальное окно ингредиента')
    def ingredient_modal_window_is_displayed(self):
        return self.wait_for_element(MainPageLocators.modal_window_locator).is_displayed()

    @allure.step('Закрылось модальное окно ингредиента')
    def ingredient_modal_window_is_closed(self):
        return self.find_element(MainPageLocators.modal_window_locator)

    @allure.step('Открылось модальное окно заказа')
    def order_modal_window_is_displayed(self):
        return self.wait_for_element(MainPageLocators.order_modal_window_locator).is_displayed()

    @allure.step('Отображается блок с деталями ингредиента')
    def ingredient_detail_block_is_displayed(self):
        return self.wait_for_element(MainPageLocators.detail_info_modal_window_locator).is_displayed()

    @allure.step('Получить текст "Ваш заказ начали готовить"')
    def get_starting_order_text(self):
        return self.get_text_element(MainPageLocators.order_being_prepared_text_locator)

    @allure.step('Получить значение счетчика ингредиента')
    def get_value_ingredient_counter(self):
        return self.get_text_element(MainPageLocators.bun_counter_locator)

    @allure.step('Получить значение счетчика ингредиента')
    def get_total_sum_order(self):
        return self.get_text_element(MainPageLocators.total_sum_locator)
