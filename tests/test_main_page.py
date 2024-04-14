from locators.main_page_locators import MainPageLocators
from user import User


class TestMainPage:
    user = User()
    user_data = []

    @classmethod
    def setup_class(cls):
        cls.user_data = cls.user.create_new_user()

    def test_click_to_ingredient(self, main_page):
        main_page.click_to_ingredient()
        assert ((main_page.wait_for_element(MainPageLocators.modal_window_locator)
                 and main_page.wait_for_element(MainPageLocators.detail_title_in_modal_window_locator))
                and main_page.wait_for_element(MainPageLocators.detail_info_modal_window_locator))

    def test_close_ingredient_modal_window(self, main_page):
        main_page.click_to_ingredient()
        main_page.wait_for_element(MainPageLocators.modal_window_locator)
        main_page.close_modal_window()
        assert not main_page.find_element(MainPageLocators.modal_window_locator)

    def test_adding_ingredient_for_order(self, main_page):
        main_page.adding_ingredient_for_order()
        assert (main_page.get_text_element(MainPageLocators.bun_counter_locator) == '2'
                and main_page.get_text_element(MainPageLocators.total_sum_locator) == '1976')

    def test_ordering_with_auth_user(self, header_page, main_page, login_page):
        header_page.click_to_personal_account()
        login_page.login(self.user_data[0], self.user_data[1])
        main_page.click_on_element(MainPageLocators.place_order_button_locator)
        assert (main_page.wait_for_element(MainPageLocators.order_modal_window)
                and main_page.wait_for_element(MainPageLocators.order_being_prepared_text_locator))

    @classmethod
    def teardown_class(cls):
        cls.user.delete_user(cls.user_data[3])
