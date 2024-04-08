from selenium.webdriver.common.by import By


class HeaderPageLocators:
    personal_account_locator = [By.XPATH, ".//p[text()='Личный Кабинет']"]
    order_feed_locator = [By.XPATH, ".//p[text()='Лента Заказов']"]
    constructor_locator = [By.XPATH, ".//p[text()='Конструктор']"]
