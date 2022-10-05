import pytest
from Pages.LoginPage import LoginPage
from Config.config import TestData
import time


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class Test_Login(BaseTest):
    def test_email_fail(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.click_sign_in()
        self.loginPage.submit_email(TestData.EMAIL_F)
        flag = self.loginPage.get_message()
        assert flag

    def test_create_success(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.click_sign_in()
        self.loginPage.submit_email(TestData.EMAIL)
        self.loginPage.create_account(TestData.CUSTOMER_FIRST_NAME,
                                      TestData.CUSTOMER_LAST_NAME,
                                      TestData.PASSWORD,
                                      TestData.ADDRESS,
                                      TestData.CITY,
                                      TestData.ID_STATE,
                                      TestData.POSTCODE,
                                      TestData.ID_COUNTRY,
                                      TestData.PHONE_MOBILE)
