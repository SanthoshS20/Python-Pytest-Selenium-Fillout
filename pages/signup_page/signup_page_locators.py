from pages.base_page.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By

class SignupPageLocators(BasePageLocators):
  EMAIL_ID_LOCATOR = (By.XPATH, '//input[@type="email"]')
  PASSWORD_LOCATOR = (By.XPATH, '//input[@type="password"]')
  SIGNUP_BUTTON_LOCATOR = (By.XPATH, '//button[@type="submit"]')
  FIRST_NAME_LOCATOR = (By.XPATH, '//input[@data-cy="signup-firstName-input"]')
  LAST_NAME_LOCATOR = (By.XPATH, '//input[@data-cy="signup-lastName-input"]')
  FINISH_SIGNUP_BUTTON_LOCATOR = (By.XPATH, '//span[text()="Finish sign up"]')
  HOME_BUTTON_LOCATOR = (By.XPATH, '//div[@data-cy="new-flow-home-button"]')
  CREATE_ACCOUNT_LABEL = (By.XPATH, '//h2[text()="Create your free account"]')