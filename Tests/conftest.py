import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Utilities import ReadConfigurations


@pytest.fixture
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="invalid_product", attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="class")
def setup(request):
    global driver
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
