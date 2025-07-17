from selenium.webdriver.common.by import By
import base64

from pages.BasePage import BasePage


class LoginPage(BasePage):

   # WebElements
    username_textfield = (By.ID,'username')
    password_textfield = (By.ID,'password')
    submit_btn = (By.ID,'submit')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

   #Page supporting methods
    def load_application(self,url):
        self.driver.get(url)

    def do_login(self,username,password):
        # decoding the encoded password
        decoded_password = base64.b64decode(password).decode("utf-8")
        self.do_enter(self.username_textfield,username)
        self.do_enter(self.password_textfield,decoded_password)
        self.do_click(self.submit_btn)
