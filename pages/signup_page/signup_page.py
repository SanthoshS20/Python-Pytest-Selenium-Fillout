from pages.base_page.base_page import BasePage
from pages.signup_page.signup_page_locators import SignupPageLocators

class SignupPage(BasePage):

  def __init__(self, driver):
    self.driver = driver
    super().__init__(driver)

  def enter_email(self, email_address):
    self.enter_text(SignupPageLocators.EMAIL_ID_LOCATOR, email_address)

  def enter_password(self, password):
    self.enter_text(SignupPageLocators.PASSWORD_LOCATOR, password)

  def click_signup_button(self):
    self.click_webelement(SignupPageLocators.SIGNUP_BUTTON_LOCATOR)

  def enter_firstname(self, firstname):
    self.enter_text(SignupPageLocators.FIRST_NAME_LOCATOR, firstname)

  def enter_lastname(self, lastname):
    self.enter_text(SignupPageLocators.LAST_NAME_LOCATOR, lastname)

  def click_finish_signup_button(self):
    self.click_webelement(SignupPageLocators.FINISH_SIGNUP_BUTTON_LOCATOR)

  def click_home_button(self):
    self.wait_until_element_is_visible(SignupPageLocators.HOME_BUTTON_LOCATOR,10)
    self.click_element_js(self.get_webelement(SignupPageLocators.HOME_BUTTON_LOCATOR))
    # self.click_webelement(SignupPageLocators.HOME_BUTTON_LOCATOR)

  def verify_create_account_label(self):
    self.wait_until_element_is_visible(SignupPageLocators.CREATE_ACCOUNT_LABEL, 10)