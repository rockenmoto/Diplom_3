from selenium.webdriver.common.by import By


class LoginPageLocators:
    email_input_locator = [By.XPATH, ".//label[text() = 'Email']/following-sibling::input"]
    pass_input_locator = [By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input"]
    login_button_locator = [By.XPATH, './/button[text()="Войти"]']
    restore_pass_locator = [By.XPATH, './/a[text()="Восстановить пароль"]']
