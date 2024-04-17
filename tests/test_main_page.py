import allure
import pytest

from locators.main_page_locators import MainPageLocators
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from user import User


class TestMainPage:
    user = User()
    user_data = []

    @classmethod
    def setup_class(cls):
        cls.user_data = cls.user.create_new_user()

    @allure.title('Проверка появления всплывающего окна с деталями при клике на Ингредиент')
    @pytest.mark.parametrize("selected_driver", ['driver_chrome', 'driver_firefox'])
    def test_click_to_ingredient(self, request, selected_driver):
        driver = request.getfixturevalue(selected_driver)
        main_page = MainPage(driver)

        main_page.click_to_ingredient()
        assert ((main_page.wait_for_element(MainPageLocators.modal_window_locator)
                 and main_page.wait_for_element(MainPageLocators.detail_title_in_modal_window_locator))
                and main_page.wait_for_element(MainPageLocators.detail_info_modal_window_locator))

    @allure.title('Проверка закрытия всплывающего окна кликом по крестику')
    @pytest.mark.parametrize("selected_driver", ['driver_chrome', 'driver_firefox'])
    def test_close_ingredient_modal_window(self, request, selected_driver):
        driver = request.getfixturevalue(selected_driver)
        main_page = MainPage(driver)

        main_page.click_to_ingredient()
        main_page.wait_for_element(MainPageLocators.modal_window_locator)
        main_page.close_modal_window()
        assert not main_page.find_element(MainPageLocators.modal_window_locator)

    @allure.title('Проверка увеличения счетчика при добавлении ингредиента в заказ')
    @pytest.mark.parametrize("selected_driver", ['driver_chrome', 'driver_firefox'])
    def test_adding_ingredient_for_order(self, request, selected_driver):
        driver = request.getfixturevalue(selected_driver)
        main_page = MainPage(driver)

        main_page.adding_ingredient_for_order()
        assert (main_page.get_text_element(MainPageLocators.bun_counter_locator) == '2'
                and main_page.get_text_element(MainPageLocators.total_sum_locator) == '1976')

    @allure.title('Проверка залогиненный пользователь может оформить заказ')
    @pytest.mark.parametrize("selected_driver", ['driver_chrome', 'driver_firefox'])
    def test_ordering_with_auth_user(self, request, selected_driver):
        driver = request.getfixturevalue(selected_driver)
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        login_page = LoginPage(driver)

        header_page.click_to_personal_account()
        login_page.login(self.user_data[0], self.user_data[1])
        main_page.click_to_checkout_button()
        assert (main_page.wait_for_element(MainPageLocators.order_modal_window_locator)
                and main_page.wait_for_element(MainPageLocators.order_being_prepared_text_locator))

    @classmethod
    def teardown_class(cls):
        cls.user.delete_user(cls.user_data[3])
