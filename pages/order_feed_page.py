import allure

from locators.header_page_locators import HeaderPageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step('Receiving an order number')
    def get_order_id(self):
        return self.get_text_element(OrderFeedPageLocators.last_order_id_locator)

    @allure.step('Retrieving an order number from the page "Order history"')
    def get_order_id_from_history_order_page(self, main_page, personal_page, header_page):
        main_page.adding_ingredient_for_order()
        main_page.click_on_element(MainPageLocators.checkout_button_locator)
        main_page.close_modal_window()
        header_page.click_to_personal_account()
        personal_page.click_on_history_order_section()
        return personal_page.get_order_id()

    @allure.step('Obtaining value before creating an order')
    def get_before_counter_value(self, header_page):
        before_counter_data = {}
        header_page.click_on_element(HeaderPageLocators.order_feed_locator)
        before_counter_data['before_alltime_counter'] = self.get_text_element(
            OrderFeedPageLocators.order_feed_all_time_number_locator)
        before_counter_data['before_today_counter'] = self.get_text_element(
            OrderFeedPageLocators.order_feed_today_number_locator)
        return before_counter_data

    @allure.step('Receiving value after creating an order')
    def get_after_counter_value(self, header_page):
        after_counter_data = {}
        header_page.click_on_element(HeaderPageLocators.order_feed_locator)
        after_counter_data['after_alltime_counter'] = self.get_text_element(
            OrderFeedPageLocators.order_feed_all_time_number_locator)
        after_counter_data['after_today_counter'] = self.get_text_element(
            OrderFeedPageLocators.order_feed_today_number_locator)
        return after_counter_data

    @allure.step('Wait for the order to appear in the block "In the works."')
    def wait_order_in_work(self, text):
        if self.get_text_element(OrderFeedPageLocators.in_work_locator) == 'Все текущие заказы готовы!':
            self.wait_for_text_presented(OrderFeedPageLocators.in_work_locator, text)
            return self.get_text_element(OrderFeedPageLocators.in_work_locator)
        else:
            return self.get_text_element(OrderFeedPageLocators.in_work_locator)

    @allure.step('Click on the box with the order')
    def click_to_cell_order(self):
        self.click_on_element(OrderFeedPageLocators.order_list_locator)

    @allure.step('Order modal window opened')
    def order_modal_window_is_displayed(self):
        return self.wait_for_element(OrderFeedPageLocators.modal_window_locator).is_displayed()

    @allure.step('The block with the order composition is displayed')
    def order_detail_block_is_displayed(self):
        return self.wait_for_element(OrderFeedPageLocators.modal_ingredient_list_locator).is_displayed()
