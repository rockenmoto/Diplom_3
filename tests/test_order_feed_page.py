import allure
import pytest

from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_page import PersonalPage
from user import User


class TestOrderFeedPage:
    user = User()
    user_data = []

    @classmethod
    def setup_method(cls):
        cls.user_data = cls.user.create_new_user()

    @allure.title('Checking if a pop-up window with details opens when you click on an order')
    @pytest.mark.parametrize("selected_driver", ['driver_chrome', 'driver_firefox'])
    def test_open_detail_window_order_true(self, request, selected_driver):
        driver = request.getfixturevalue(selected_driver)
        header_page = HeaderPage(driver)
        order_feed_page = OrderFeedPage(driver)

        header_page.click_to_order_feed()
        order_feed_page.click_to_cell_order()
        assert order_feed_page.order_modal_window_is_displayed()
        assert order_feed_page.order_detail_block_is_displayed()

    @allure.title('Checking user order from the section «Order history» are displayed on the page «Order feed»')
    @pytest.mark.parametrize("selected_driver", ['driver_chrome', 'driver_firefox'])
    def test_order_id_the_same_for_history_and_feed_true(self, request, selected_driver):
        driver = request.getfixturevalue(selected_driver)
        header_page = HeaderPage(driver)
        order_feed_page = OrderFeedPage(driver)
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        personal_page = PersonalPage(driver)

        header_page.click_to_personal_account()
        login_page.login(self.user_data[0], self.user_data[1])
        order_id_from_history_page = order_feed_page.get_order_id_from_history_order_page(main_page, personal_page,
                                                                                          header_page)
        header_page.click_to_order_feed()
        last_order_id_two = order_feed_page.get_order_id()
        assert order_id_from_history_page == last_order_id_two

    @allure.title('Check when creating a new order counter «Completed for all time», «Executed today» increases')
    @pytest.mark.parametrize("selected_driver", ['driver_chrome', 'driver_firefox'])
    def test_all_time_counter_completed_increases_true(self, request, selected_driver):
        driver = request.getfixturevalue(selected_driver)
        header_page = HeaderPage(driver)
        order_feed_page = OrderFeedPage(driver)
        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        header_page.click_to_personal_account()
        login_page.login(self.user_data[0], self.user_data[1])

        before_counter_data = order_feed_page.get_before_counter_value(header_page)
        header_page.click_to_main_logo()
        main_page.adding_ingredient_for_order()
        main_page.click_to_checkout_button()
        main_page.close_modal_window()

        after_counter_data = order_feed_page.get_after_counter_value(header_page)
        assert after_counter_data['after_alltime_counter'] > before_counter_data['before_alltime_counter']
        assert after_counter_data['after_today_counter'] > before_counter_data['before_today_counter']

    @allure.title('Checking After an order is placed, its number appears in the In Progress section')
    @pytest.mark.parametrize("selected_driver", ['driver_chrome', 'driver_firefox'])
    def test_order_id_shows_in_in_work_true(self, request, selected_driver):
        driver = request.getfixturevalue(selected_driver)
        header_page = HeaderPage(driver)
        order_feed_page = OrderFeedPage(driver)
        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        header_page.click_to_personal_account()
        login_page.login(self.user_data[0], self.user_data[1])

        header_page.click_to_main_logo()
        main_page.adding_ingredient_for_order()
        main_page.click_to_checkout_button()
        main_page.close_modal_window()

        after_counter_data = order_feed_page.get_after_counter_value(header_page)
        in_work_order_id = order_feed_page.wait_order_in_work(after_counter_data['after_alltime_counter'])
        assert after_counter_data['after_alltime_counter'] in in_work_order_id

    @classmethod
    def teardown_method(cls):
        cls.user.delete_user(cls.user_data[3])
