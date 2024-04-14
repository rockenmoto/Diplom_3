from locators.main_page_locators import MainPageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from locators.header_page_locators import HeaderPageLocators


class TestOrderFeedPage:
    def test_open_detail_window_order_true(self, header_page, order_feed_page):
        header_page.click_on_element(HeaderPageLocators.order_feed_locator)
        order_feed_page.click_on_element(OrderFeedPageLocators.order_list_locator)
        assert (order_feed_page.wait_for_element(OrderFeedPageLocators.modal_ingredient_title_locator) and
                order_feed_page.wait_for_element(OrderFeedPageLocators.modal_ingredient_list_locator))

    def test_get_order_id(self, header_page, main_page, login, personal_page, order_feed_page):
        main_page.adding_ingredient_for_order()
        main_page.click_on_element(MainPageLocators.place_order_button_locator)
        main_page.close_modal_window()
        personal_page.click_on_history_order_section()
        last_order_id = personal_page.get_order_id()
        header_page.click_on_element(HeaderPageLocators.order_feed_locator)
        last_order_id_two = order_feed_page.get_order_id()
        assert last_order_id == last_order_id_two
