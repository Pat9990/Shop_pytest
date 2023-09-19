import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdrivermanager.gecko import GeckoDriverManager
from webdrivermanager.chrome import ChromeDriverManager


# @pytest.fixture(params=["chrome","firefox"])
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    # browser=request.params
    print(f"Creating {browser} driver")
    if browser == 'chrome':
        my_driver = webdriver.Chrome() #użycie chroma
    elif browser == 'firefox':
        my_driver = webdriver.Firefox()  # uzycie firefoxa
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox' but got {browser}")
    my_driver.implicitly_wait(10)
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.close()

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
    )
