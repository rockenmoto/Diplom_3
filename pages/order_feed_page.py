from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):
    def get_order_id(self):
        return self.get_text_element(OrderFeedPageLocators.last_order_id_locator)
