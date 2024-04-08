from selenium.webdriver.common.by import By


class MainPageLocators:
    first_bun_locator = [By.XPATH, './/p[text()="Флюоресцентная булка R2-D3"]']
    detail_title_in_popup = [By.XPATH, './/h2[text()="Детали ингредиента"]']
    ingredient_title_in_popup = [By.XPATH, './/p[text()="Флюоресцентная булка R2-D3"]']
    order_feed_title_locator = [By.XPATH, ".//h1[text()='Лента заказов']"]
    constructor_title_locator = [By.XPATH, ".//h1[text()='Соберите бургер']"]
