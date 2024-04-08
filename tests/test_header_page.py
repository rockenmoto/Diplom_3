import pytest
from locators.header_page_locators import HeaderPageLocators
from locators.main_page_locators import MainPageLocators


class TestHeaderPage:
    @pytest.mark.parametrize("section_locator, expected_result",
                             [(HeaderPageLocators.order_feed_locator, MainPageLocators.order_feed_title_locator),
                              (HeaderPageLocators.constructor_locator, MainPageLocators.constructor_title_locator)
                              ])
    def test_open_section_from_header(self, header_page, main_page, section_locator, expected_result):
        header_page.click_on_element(section_locator)
        assert main_page.wait_for_element(expected_result)
