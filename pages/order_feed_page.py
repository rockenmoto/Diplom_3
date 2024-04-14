import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


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
