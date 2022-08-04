import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--headless', action='store', default="false", dest='headless')


@pytest.fixture(scope='session')
def init_driver(request):
    options = Options()
    if request.config.getoption('headless')=='true':
        options.headless = True
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.implicitly_wait(25)
    else:
        options.add_argument("--nocache")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.implicitly_wait(30)

    driver.maximize_window()
    yield driver
    driver.quit()
