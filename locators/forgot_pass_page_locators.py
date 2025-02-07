from selenium.webdriver.common.by import By


class ForgotPassPageLocators:
    email_input_locator = [By.XPATH, ".//label[text() = 'Email']/following-sibling::input"]
    restore_button_locator = [By.XPATH, './/button[text()="Восстановить"]']
