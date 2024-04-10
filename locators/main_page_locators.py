from selenium.webdriver.common.by import By


class MainPageLocators:
    bun_locator = [By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']"]
    modal_window_locator = [By.XPATH, ".//section[contains(@class,'Modal_modal_opened')]"]
    detail_title_in_modal_window_locator = [By.XPATH, './/h2[text()="Детали ингредиента"]']
    detail_info_modal_window_locator = [By.CLASS_NAME, "Modal_modal__statsList__6cEm5"]
    close_modal_window_button = [By.XPATH, ".//section[contains(@class,'Modal_modal_opened')]/div[1]/button"]

    order_feed_title_locator = [By.XPATH, ".//h1[text()='Лента заказов']"]
    constructor_title_locator = [By.XPATH, ".//h1[text()='Соберите бургер']"]
