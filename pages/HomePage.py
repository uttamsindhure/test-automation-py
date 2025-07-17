from selenium.webdriver.common.by import By


from pages.BasePage import BasePage


class HomePage(BasePage):

   # WebElements
    logout_btn = (By.XPATH,"//a[contains(@href,'test-login')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

   #Page supporting methods
    def is_login_success(self):
        return self.is_visible(self.logout_btn)