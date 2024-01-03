from utils.utilities import Utilities
import constants, logging, pytest
from pages.home_page.home_page import HomePage
from pages.login_page.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
class TestHomePage:

  def setup_class(self):
    self.utils = Utilities(__name__, logging.DEBUG)
    self.logs = self.utils.get_logger()

  def setup_method(self, method):
    self.home = HomePage(self.driver)
    self.login = LoginPage(self.driver)
    self.login.load_page(constants.BASE_URL)
    self.login.enter_email_address(constants.EMAIL_ADDRESS)
    self.login.enter_password(constants.PASSWORD)
    self.login.click_signin_button()
    self.login.click_home_button()
    self.home.check_home_workspace_visibility()

  def teardown_method(self, method):
    self.home.click_home_page_account_menu()
    self.home.click_logout_button()
    self.login.verify_login_page_elements_visibility()

  @pytest.mark.home_test
  def test_add_new_workspace(self):
    self.home.click_add_workspace_button()
    self.home.enter_workspace_name(constants.WORKSPACE_NAME)
    self.home.click_create_workspace()
    self.home.verify_workspace_created()
    self.home.select_workspace()
    self.home.click_workspace_settings()
    self.home.click_delete_workspace()
    self.home.check_delete_workspace_checkbox()
    self.home.click_delete_workspace_in_dialog()

  def test_invite_collaborators(self):
    pass

  def test_create_new_form(self):
    pass