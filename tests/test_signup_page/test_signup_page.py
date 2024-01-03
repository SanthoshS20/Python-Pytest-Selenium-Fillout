import logging

import pytest, constants, logging
from pages.signup_page.signup_page import SignupPage
from pages.login_page.login_page import LoginPage
from pages.home_page.home_page import HomePage
from utils.utilities import Utilities


@pytest.mark.usefixtures("setup_teardown")
class TestSignupPage:

  def setup_method(self, method):
    self.signup = SignupPage(self.driver)
    self.login = LoginPage(self.driver)
    self.home = HomePage(self.driver)
    self.utils = Utilities(__name__, logging.DEBUG)
    self.logs = self.utils.get_logger()
    # self.driver.delete_all_cookies()
    self.login.load_page(constants.BASE_URL)
    self.logs.info("Page Load Successful.")
    
  def teardown_method(self, method):
    self.driver.delete_all_cookies()

  def test_signup_with_valid_credentials(self):
    self.login.click_signup_link()
    self.logs.debug("Signup button is clicked.")
    self.signup.verify_create_account_label()
    assert self.signup.get_current_url() == constants.BASE_URL + "signup", f"URL mismatched. Expected URL {constants.BASE_URL}signup"
    self.signup.enter_email(constants.EMAIL_ADDRESS)
    self.logs.debug(f"Email Address {constants.EMAIL_ADDRESS} is entered.")
    self.signup.enter_password(constants.PASSWORD)
    self.logs.debug(f"Password {constants.PASSWORD} is entered.")
    self.signup.click_signup_button()
    self.logs.debug("Clicked Signup Button.")
    self.signup.enter_firstname(constants.FIRST_NAME)
    self.logs.debug(f"First Name {constants.FIRST_NAME} is entered.")
    self.signup.enter_lastname(constants.LAST_NAME)
    self.logs.debug(f"Last Name {constants.LAST_NAME} is entered.")
    self.signup.click_finish_signup_button()
    self.logs.debug("Clicked Signup Button.")
    self.signup.click_home_button()
    self.logs.debug("Clicked Home Icon.")
    self.home.check_home_workspace_visibility()
    assert self.signup.get_current_url() == constants.BASE_URL + "home"
