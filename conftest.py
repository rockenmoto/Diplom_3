import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver_chrome(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def driver_firefox(request):
    driver = webdriver.Firefox()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()
