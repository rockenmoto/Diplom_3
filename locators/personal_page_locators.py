from selenium.webdriver.common.by import By


class PersonalPageLocators:
    login_button_locator = [By.XPATH, './/button[text()="Войти"]']
    logout_button_locator = [By.XPATH, './/button[text()="Выход"]']
    email_input_locator = [By.XPATH, ".//label[text() = 'Email']/following-sibling::input"]
    password_input_locator = [By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input"]
