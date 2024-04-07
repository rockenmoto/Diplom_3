from selenium.webdriver.common.by import By


class PersonalPageLocators:
    logout_button_locator = [By.XPATH, './/button[text()="Выход"]']
    order_history_locator = [By.XPATH, './/a[text()="История заказов"]']
