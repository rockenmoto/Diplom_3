import allure
import pytest

from locators.header_page_locators import HeaderPageLocators
from locators.main_page_locators import MainPageLocators
from pages.header_page import HeaderPage
from pages.main_page import MainPage


class TestHeaderPage:
    @allure.title('Проверка переходов по клику на «Конструктор» и «Историю заказов»')
    @pytest.mark.parametrize("selected_driver, section_locator, expected_result",
                             [('driver_chrome', HeaderPageLocators.order_feed_locator,
                               MainPageLocators.order_feed_title_locator),
                              ('driver_chrome', HeaderPageLocators.order_feed_locator,
                               MainPageLocators.order_feed_title_locator),
                              ('driver_firefox', HeaderPageLocators.constructor_locator,
                               MainPageLocators.constructor_title_locator),
                              ('driver_firefox', HeaderPageLocators.constructor_locator,
                               MainPageLocators.constructor_title_locator)],
                             )
    def test_open_section_from_header(self, request, selected_driver, section_locator, expected_result):
        driver = request.getfixturevalue(selected_driver)
        header_page = HeaderPage(driver)
        main_page = MainPage(driver)

        header_page.click_on_element(section_locator)
        assert main_page.wait_for_element(expected_result)
