from venv import logger

from tests.functionalTest.test_base import BaseTest


class TestLogin(BaseTest):

    def test_load_application(self,config_data,setup_class_objects):
        login_page,_ = setup_class_objects
        login_page.load_application(config_data['PAGE_URL'])

    def test_sign_up(self, config_data,setup_class_objects):
        login_page,home_page = setup_class_objects
        login_page.do_login(config_data['USERNAME'],config_data['PASSWORD'])
        assert home_page.is_login_success()
        logger.info("Login successful")

