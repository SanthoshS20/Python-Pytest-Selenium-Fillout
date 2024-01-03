from pages.base_page.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By

class FormPageLocators(BasePageLocators):
  FORM_NAME_LOCATOR = (By.XPATH, '//div[@data-cy="rename-flow-modal-input"]//input[@data-cy="input-component"]')
  CONTINUE_BUTTON_LOCATOR = (By.XPATH, '//span[text()="Continue"]')
  PREVIEW_BUTTON_LOCATOR = (By.XPATH, '//span[text()="Preview"]')
  PUBLISH_BUTTON_LOCATOR = (By.XPATH, '//span[text()="Publish"]')