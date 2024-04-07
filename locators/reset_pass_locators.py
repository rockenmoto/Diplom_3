from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ResetPassPageLocators(BasePage):
    save_button_locator = [By.XPATH, './/button[text()="Сохранить"]']
    eye_icon = [By.XPATH, './/div[@class="input__icon input__icon-action"]']
    pass_input = './/fieldset[1][@class="Auth_fieldset__1QzWN mb-6"]/div/div'
