import constants
from pages.base_page.base_page import BasePage
from pages.login_page.login_page_locators import LoginPageLocators

class LoginPage(BasePage):

  def __init__(self, driver):
    self.driver = driver
    super().__init__(self.driver)

  def enter_email_address(self, email_address):
    # self.element = self.get_webelement(LoginPageLocators.EMAIL_ID_LOCATOR)
    # self.set_input_value(self.element, constants.EMAIL_ADDRESS)
    self.enter_text(LoginPageLocators.EMAIL_ID_LOCATOR, email_address)

  def enter_password(self, password):
    self.enter_text(LoginPageLocators.PASSWORD_LOCATOR, password)

  def click_signin_button(self):
    self.click_webelement(LoginPageLocators.SIGNIN_BUTTON_LOCATOR)

  def click_home_button(self):
    self.wait_until_element_is_visible(LoginPageLocators.HOME_BUTTON_LOCATOR, 10)
    self.click_element_js(self.get_webelement(LoginPageLocators.HOME_BUTTON_LOCATOR))

  def load_page(self, url):
    super().load_page(url)
    self.wait_until_element_is_visible(LoginPageLocators.SIGNUP_LINK_LOCATOR, 10)
    self.wait_until_element_is_visible(LoginPageLocators.EMAIL_ID_LOCATOR, 10)
    self.wait_until_element_is_visible(LoginPageLocators.PASSWORD_LOCATOR, 10)
    self.wait_until_element_is_visible(LoginPageLocators.SIGNIN_BUTTON_LOCATOR, 10)

  def click_signup_link(self):
    self.click_webelement(LoginPageLocators.SIGNUP_LINK_LOCATOR)

  def get_invalid_credentials_message(self):
    return self.get_text(LoginPageLocators.INCORRECT_CREDENTIALS_MESSAGE_LOCATOR)

  def verify_login_page_elements_visibility(self):
    self.wait_until_element_is_visible(LoginPageLocators.SIGNIN_BUTTON_LOCATOR, 10)
    self.wait_until_element_is_visible(LoginPageLocators.SIGNIN_LABEL, 10)