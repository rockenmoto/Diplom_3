from selenium.webdriver.common.by import By


class MainPageLocators:
    bun_locator = [By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']"]
    bun_counter_locator = [By.XPATH, ".//section[1]/div[2]/ul[1]/a[1]/div[1]/p"]
    modal_window_locator = [By.XPATH, ".//section[contains(@class,'Modal_modal_opened')]"]
    detail_title_in_modal_window_locator = [By.XPATH, './/h2[text()="Детали ингредиента"]']
    detail_info_modal_window_locator = [By.CLASS_NAME, "Modal_modal__statsList__6cEm5"]
    total_sum_locator = [By.XPATH, ".//div[contains(@class,'totalContainer')]/p"]
    close_modal_window_button_locator = [By.XPATH, ".//section[contains(@class,'Modal_modal_opened')]/div[1]/button"]

    place_order_button_locator = [By.XPATH, './/button[text()="Оформить заказ"]']
    order_modal_window_locator = [By.XPATH, ".//div[contains(@class,'Modal_modal__container')]"]
    order_being_prepared_text_locator = [By.XPATH, ".//p[text()='Ваш заказ начали готовить']"]

    order_feed_title_locator = [By.XPATH, ".//h1[text()='Лента заказов']"]
    constructor_title_locator = [By.XPATH, ".//h1[text()='Соберите бургер']"]
    buns_constructor_locator = [By.CLASS_NAME, "BurgerConstructor_basket__list__l9dp_"]
