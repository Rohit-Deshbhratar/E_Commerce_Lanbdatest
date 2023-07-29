import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Utilities import ReadConfigurations


@pytest.fixture(scope="class")
def setup(request):
    driver = None
    browser = ReadConfigurations.read_configuration("basic info", "browser")
    if browser.__eq__("firefox"):
        options = Options()
        driver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))
    elif browser.__eq__("chrome"):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    else:
        print("Please select only CHROME or FIREFOX browser")
    driver.maximize_window()
    app_url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
