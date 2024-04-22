import pytest
from selenium import webdriver
from urls import Urls


@pytest.fixture(scope='function')
def driver_chrome(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Urls.base_url)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def driver_firefox(request):
    driver = webdriver.Firefox()
    driver.get(Urls.base_url)
    yield driver
    driver.quit()
