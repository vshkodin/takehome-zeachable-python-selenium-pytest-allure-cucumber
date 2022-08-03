import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--headless', action='store', default="false", dest='headless')


@pytest.fixture(scope='session')
def init_driver(request):
    options = Options()
    if request.config.getoption('headless')=='true':
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(25)
    else:
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(25)
    driver.maximize_window()
    yield driver
    driver.quit()