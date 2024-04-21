from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    order_list_locator = [By.XPATH, ".//ul[@class = 'OrderFeed_list__OLh59']/li[1]"]
    modal_window_locator = [By.XPATH, ".//section[contains(@class,'opened')]/div[contains(@class,'container')]"]
    modal_ingredient_title_locator = [By.XPATH, ".//p[text()='Cостав']"]
    modal_ingredient_list_locator = [By.XPATH, ".//ul[@class = 'Modal_list__2sHWc']"]
    last_order_id_locator = [By.XPATH, ".//ul/li[1]//p[@class = 'text text_type_digits-default']"]
    order_feed_all_time_number_locator = [By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p"]
    order_feed_today_number_locator = [By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p"]
    in_work_locator = [By.XPATH, ".//ul[contains(@class,'orderListReady__1YFem')]/li"]
