import constants
from pages.base_page.base_page import BasePage
from pages.home_page.home_page_locators import HomePageLocators
from pages.login_page.login_page_locators import LoginPageLocators

class HomePage(BasePage):

  def __init__(self, driver):
    self.driver = driver
    super().__init__(driver)
    
  def click_home_page_account_menu(self):
    self.click_webelement(HomePageLocators.ACCOUNT_MENU_LOCATOR)

  def click_logout_button(self):
    self.click_webelement(HomePageLocators.LOGOUT_MENU_LOCATOR)

  def click_settings_menu(self):
    self.click_webelement(HomePageLocators.SETTINGS_MENU_LOCATOR)

  def click_add_workspace_button(self):
    self.click_webelement(HomePageLocators.ADD_WORKSPACE_LOCATOR)

  def enter_workspace_name(self, name):
    self.enter_text(HomePageLocators.WORKSPACE_NAME_LOCATOR, name)

  def click_create_workspace(self):
    self.click_webelement(HomePageLocators.CREATE_WORKSPACE_BUTTON_LOCATOR)

  def verify_workspace_created(self):
    self.wait_until_element_is_visible(HomePageLocators.NEW_WORKSPACE_NAVIGATION_LOCATOR, 10)

  def check_home_workspace_visibility(self):
    self.wait_until_element_is_visible(HomePageLocators.HOME_WORKSPACE_LOCATOR, 10)

  def select_workspace(self):
    self.click_webelement(HomePageLocators.NEW_WORKSPACE_NAVIGATION_LOCATOR)
    self.wait_until_element_is_visible(HomePageLocators.NEW_WORKSPACE_HEADER_LOCATED, 10)

  def click_workspace_settings(self):
    self.click_webelement(HomePageLocators.WORKSPACE_SETTINGS_LOCATOR)
    self.wait_until_element_is_visible(HomePageLocators.DELETE_WORKSPACE_BUTTON_LOCATOR, 15)

  def click_delete_workspace(self):
    self.click_webelement(HomePageLocators.DELETE_WORKSPACE_BUTTON_LOCATOR)
    self.wait_until_element_is_visible(HomePageLocators.DELETE_WORKSPACE_POPUP_DIALOG_LABEL_LOCATOR, 10)
    # self.wait_until_element_is_visible(HomePageLocators.DELETE_WORKSPACE_BUTTON_IN_DIALOG_LOCATOR, 10)

  def check_delete_workspace_checkbox(self):
    self.click_webelement(HomePageLocators.DELETE_CONFIRM_CHECKBOX_LOCATOR)
    self.wait_until_element_should_be_enabled(HomePageLocators.DELETE_WORKSPACE_BUTTON_IN_DIALOG_LOCATOR, 10)

  def click_delete_workspace_in_dialog(self):
    self.click_webelement(HomePageLocators.DELETE_WORKSPACE_BUTTON_IN_DIALOG_LOCATOR)
    self.wait_until_element_should_not_be_visible(HomePageLocators.NEW_WORKSPACE_NAVIGATION_LOCATOR, 10)

  def click_add_collaborators(self):
    self.click_webelement(HomePageLocators.ADD_COLLABORATOR_LOCATOR)
    self.wait_until_element_is_visible(HomePageLocators.INVITE_COLLABORATORS_LABEL_IN_DIALOG_LOCATOR, 10)

  def enter_email_address_in_invite_collaborators(self, email):
    self.enter_text(HomePageLocators.EMAIL_ADDRESS_IN_INVITE_COLLABORATORS_FIELD_LOCATOR, email)

