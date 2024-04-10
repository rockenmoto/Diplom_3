from locators.main_page_locators import MainPageLocators
from locators.header_page_locators import HeaderPageLocators


class TestMainPage:
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
