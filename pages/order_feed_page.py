import time

import allure

from locators.header_page_locators import HeaderPageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step('Получение номера заказа')
    def get_order_id(self):
        return self.get_text_element(OrderFeedPageLocators.last_order_id_locator)

    @allure.step('Получение номера заказа со страницы "История заказов"')
    def get_order_id_from_history_order_page(self, main_page, personal_page, header_page):
        main_page.adding_ingredient_for_order()
        main_page.click_on_element(MainPageLocators.checkout_button_locator)
        main_page.close_modal_window()
        header_page.click_to_personal_account()
        personal_page.click_on_history_order_section()
        return personal_page.get_order_id()

    @allure.step('Получение значение до создания заказа')
    def get_before_counter_value(self, header_page):
        before_counter_data = {}
        header_page.click_on_element(HeaderPageLocators.order_feed_locator)
        before_counter_data['before_alltime_counter'] = self.get_text_element(
            OrderFeedPageLocators.order_feed_all_time_number_locator)
        before_counter_data['before_today_counter'] = self.get_text_element(
            OrderFeedPageLocators.order_feed_today_number_locator)
        return before_counter_data

    @allure.step('Получение значение после создания заказа')
    def get_after_counter_value(self, header_page):
        after_counter_data = {}
        header_page.click_on_element(HeaderPageLocators.order_feed_locator)
        after_counter_data['after_alltime_counter'] = self.get_text_element(
            OrderFeedPageLocators.order_feed_all_time_number_locator)
        after_counter_data['after_today_counter'] = self.get_text_element(
            OrderFeedPageLocators.order_feed_today_number_locator)
        return after_counter_data

    @allure.step('Ожидаем появления ордера в блоке "В работе"')
    def wait_order_in_work(self):
        if self.get_text_element(OrderFeedPageLocators.in_work_locator) == 'Все текущие заказы готовы!':
            time.sleep(5)
            return self.get_text_element(OrderFeedPageLocators.in_work_locator)
        else:
            return self.get_text_element(OrderFeedPageLocators.in_work_locator)
