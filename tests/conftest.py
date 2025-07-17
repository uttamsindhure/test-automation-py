import pytest
import yaml
import datetime
from pathlib import Path
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

from pages.LoginPage import LoginPage
from pages.HomePage import HomePage


@pytest.fixture(params=["chrome"],scope='class')
def init_driver(request):
    global web_driver
    if request.param =="chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()

    request.cls.driver = web_driver
    yield
    web_driver.close()

#Reading yaml files and making access granted to all files till session ends
@pytest.fixture(scope="session")
def config_data():
    """Fixture to load configuration data from config.yaml."""
    config_path = Path(__file__).parent.parent / "config/webdriver_config.yaml"
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config


"""Customising HTML report"""
def pytest_html_report_title(report):
    report.title = "Pytest HTML Report Example"


def pytest_configure(config):
    config.stash[metadata_key]["Project"] = "Pytest With Uttam"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):


    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':

        nodeid = item.nodeid
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = f'{nodeid}_{datetime.datetime.now().strftime("%Y-%m-%d_%H_%M")}.png'.replace("/", "_").replace("::",
                                                                                                                "_").replace(
                ".py", "")
            img_path = Path(__file__).parent.parent / f"reports/src/{file_name}"
            web_driver.save_screenshot(img_path)
            screenshot = web_driver.get_screenshot_as_base64()  # the hero
            extra.append(pytest_html.extras.image(screenshot, ''))

        report.extra = extra
"""=============================="""

"""Initialising class object once per sesssion"""
@pytest.fixture(scope="class")
def setup_class_objects():
    loginPage = LoginPage(web_driver)
    homePage = HomePage(web_driver)
    return loginPage,homePage
"""====================================="""