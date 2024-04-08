from locators.main_page_locators import MainPageLocators
from locators.header_page_locators import HeaderPageLocators


class TestMainPage:
    def test_click_to_ingredient(self, main_page):
        main_page.click_to_ingredient()
        assert (main_page.wait_for_element(MainPageLocators.first_bun_locator)
                and main_page.wait_for_element(MainPageLocators.ingredient_title_in_popup))
