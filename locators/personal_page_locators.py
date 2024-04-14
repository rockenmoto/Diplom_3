from selenium.webdriver.common.by import By


class PersonalPageLocators:
    logout_button_locator = [By.XPATH, './/button[text()="Выход"]']
    order_history_locator = [By.XPATH, './/a[text()="История заказов"]']
    last_cell_order_id_locator = [By.XPATH, './/ul[contains(@class,"OrderHistory_list")]/li[last()]/a/div[1]/p[1]']
