from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    @allure.step('Ожидаем элемент')
    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Получаем текст элемента')
    def get_text_element(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    @allure.step('Скроллим до элемента')
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Заполняем поле текстом')
    def fill_in_field(self, locator, text):
        element = self.wait_for_element(locator)
        element.send_keys(text)

    @allure.step('Получаем урл страницы')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Получаем атрибут локатара для класса')
    def get_class_attribute(self, locator):
        return self.driver.find_element(By.XPATH, locator).get_attribute('class')

    @allure.step('Поиск элемента с исключением')
    def find_element(self, locator):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    @allure.step('Перемещение элемента')
    def move_element(self, locator1, locator2):
        from_element = self.wait_for_element(locator1)
        to_element = self.wait_for_element(locator2)
        ActionChains(self.driver).drag_and_drop(from_element, to_element).perform()
