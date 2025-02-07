import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Click on "Ingredient"')
    def click_to_ingredient(self):
        self.click_on_element(MainPageLocators.bun_locator)

    @allure.step('Closing a modal window with a cross')
    def close_modal_window(self):
        self.wait_for_element(MainPageLocators.close_modal_window_button_locator).is_enabled()
        self.click_on_element(MainPageLocators.close_modal_window_button_locator)

    @allure.step('Adding an ingredient for an order')
    def adding_ingredient_for_order(self):
        self.move_element(MainPageLocators.bun_locator, MainPageLocators.buns_constructor_locator)

    @allure.step('Click on the button "Place an order"')
    def click_to_checkout_button(self):
        self.click_on_element(MainPageLocators.checkout_button_locator)

    @allure.step('The ingredient modal window opened')
    def ingredient_modal_window_is_displayed(self):
        return self.wait_for_element(MainPageLocators.modal_window_locator).is_displayed()

    @allure.step('The ingredient modal window has closed')
    def ingredient_modal_window_is_closed(self):
        return self.find_element(MainPageLocators.modal_window_locator)

    @allure.step('Order modal window opened')
    def order_modal_window_is_displayed(self):
        return self.wait_for_element(MainPageLocators.order_modal_window_locator).is_displayed()

    @allure.step('The ingredient detail block is displayed')
    def ingredient_detail_block_is_displayed(self):
        return self.wait_for_element(MainPageLocators.detail_info_modal_window_locator).is_displayed()

    @allure.step('Get the text "Your order has been placed"')
    def get_starting_order_text(self):
        return self.get_text_element(MainPageLocators.order_being_prepared_text_locator)

    @allure.step('Get the value of the ingredient counter')
    def get_value_ingredient_counter(self):
        return self.get_text_element(MainPageLocators.bun_counter_locator)

    @allure.step('Get the full amount of the order')
    def get_total_sum_order(self):
        return self.get_text_element(MainPageLocators.total_sum_locator)
