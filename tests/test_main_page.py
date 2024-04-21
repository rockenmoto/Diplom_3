import allure
import pytest

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
        assert main_page.ingredient_modal_window_is_displayed()
        assert main_page.ingredient_detail_block_is_displayed()

    @allure.title('Проверка закрытия всплывающего окна кликом по крестику')
    @pytest.mark.parametrize("selected_driver", ['driver_chrome', 'driver_firefox'])
    def test_close_ingredient_modal_window(self, request, selected_driver):
        driver = request.getfixturevalue(selected_driver)
        main_page = MainPage(driver)

        main_page.click_to_ingredient()
        main_page.close_modal_window()
        assert not main_page.ingredient_modal_window_is_closed()

    @allure.title('Проверка увеличения счетчика при добавлении ингредиента в заказ')
    @pytest.mark.parametrize("selected_driver", ['driver_chrome', 'driver_firefox'])
    def test_adding_ingredient_for_order(self, request, selected_driver):
        driver = request.getfixturevalue(selected_driver)
        main_page = MainPage(driver)

        main_page.adding_ingredient_for_order()
        assert main_page.get_value_ingredient_counter() == '2'
        assert main_page.get_total_sum_order() == '1976'

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
        assert main_page.order_modal_window_is_displayed()
        assert main_page.get_starting_order_text() == 'Ваш заказ начали готовить'

    @classmethod
    def teardown_class(cls):
        cls.user.delete_user(cls.user_data[3])
