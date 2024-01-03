from pages.base_page.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By

class LoginPageLocators(BasePageLocators):
  EMAIL_ID_LOCATOR = (By.XPATH, '//input[@data-cy="signup-email-input"]')
  PASSWORD_LOCATOR = (By.XPATH, '//input[@data-cy="signup-password-input"]')
  SIGNIN_BUTTON_LOCATOR = (By.XPATH, '//button[@data-cy="email-signup-button"]')
  HOME_BUTTON_LOCATOR = (By.XPATH, '//a[@href="/home"]')
  SIGNIN_LABEL = (By.XPATH, '//div[text()="Sign in to Fillout"]')
  SIGNUP_LINK_LOCATOR = (By.LINK_TEXT, 'Sign up')
  INCORRECT_CREDENTIALS_MESSAGE_LOCATOR = (By.XPATH, '//div[contains(text(),"Incorrect")]')
