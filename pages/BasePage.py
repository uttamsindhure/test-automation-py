import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""Generic methods"""
class BasePage():
    def __init__(self,driver):
        self.driver = driver

    def do_enter(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def do_click(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()

    def is_visible(self,by_locator):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).is_displayed()