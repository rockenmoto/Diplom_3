from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    order_list_locator = [By.XPATH, ".//ul[@class = 'OrderFeed_list__OLh59']/li[1]"]
    modal_window_locator = [By.XPATH, ".//section[contains(@class,'opened')]/div[contains(@class,'container')"]
    modal_ingredient_title_locator = [By.XPATH, ".//p[text()='Cостав']"]
    modal_ingredient_list_locator = [By.CSS_SELECTOR, ".//ul[@class = 'Modal_list__2sHWc']/li"]
    last_order_id_locator = [By.XPATH, ".//ul[contains(@class,'OrderFeed_list__OLh59')]/li[1]/a/div[1]/p[1]"]
    order_feed_all_time_number_locator = [By.XPATH, ".//div[contains(@class,'1L6Iv')]/div[2]/p[2]"]
    order_feed_today_number_locator = [By.XPATH, ".//div[contains(@class,'1L6Iv')]/div[3]/p[2]"]
    in_work_locator = [By.XPATH, ".//ul[contains(@class,'orderListReady__1YFem')]/li"]
