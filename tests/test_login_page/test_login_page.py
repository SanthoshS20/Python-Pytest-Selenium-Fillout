from pages.login_page.login_page import LoginPage
from pages.home_page.home_page import HomePage
import pytest, logging, constants, time
from utils.utilities import Utilities

@pytest.mark.usefixtures("setup_teardown")
class TestLoginPage:

  def setup_class(self):
    self.utils = Utilities(__name__, logging.DEBUG)
    self.logs = self.utils.get_logger()

  def setup_method(self, method):
    self.login = LoginPage(self.driver)
    self.home = HomePage(self.driver)
    self.login.load_page(constants.BASE_URL)

  def teardown_method(self, method):
    self.driver.delete_all_cookies()

  @pytest.mark.login
  def test_login_with_valid_credentials(self):
    self.login.enter_email_address(constants.EMAIL_ADDRESS)
    self.login.enter_password(constants.PASSWORD)
    self.login.click_signin_button()
    self.login.click_home_button()
    self.home.check_home_workspace_visibility()
    self.home.click_home_page_account_menu()
    self.home.click_logout_button()
    self.login.verify_login_page_elements_visibility()

  @pytest.mark.login
  def test_login_with_invalid_credentials(self):
    self.login.enter_email_address(constants.EMAIL_ADDRESS)
    self.login.enter_password(constants.INCORRECT_PASSWORD)
    self.login.click_signin_button()
    assert self.login.get_invalid_credentials_message() == "Incorrect email or password."
