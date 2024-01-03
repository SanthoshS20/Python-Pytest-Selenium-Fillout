from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions

class BasePage:

  def __init__(self, driver):
    self.driver = driver

  def click_webelement(self, locator):
    self.driver.find_element(*locator).click()

  def get_text(self, locator):
    return self.driver.find_element(*locator).text

  def set_input_value(self, element, value):
    self.driver.execute_script("arguments[0].value = arguments[1]", element, value)

  def click_element_js(self, element):
    self.driver.execute_script("arguments[0].click()", element)

  def cget_webelement(self, locator):
    self.element = self.driver.find_element(*locator)
    return self.element

  def enter_text(self, locator, text):
    self.driver.find_element(*locator).send_keys(text)

  def web_driver_wait(self, seconds):
    self.wait = WebDriverWait(self.driver, seconds)
    return self.wait

  def wait_until_element_is_visible(self, locator, seconds):
    self.wait = self.web_driver_wait(seconds)
    self.wait.until(expected_conditions.visibility_of_element_located(locator))

  def select_dropdown_option(self, locator, option):
    self.dropdown_element = self.driver.find_element(*locator)
    self.select_element = Select(self.dropdown_element)
    self.select_element.select_by_visible_text(option)

  def get_title(self):
    return self.driver.title

  def get_current_url(self):
    return self.driver.current_url

  def load_page(self, url):
    self.driver.get(url)

  def wait_until_element_should_be_enabled(self, locator, seconds):
    self.wait = self.web_driver_wait(seconds)
    self.wait.until(expected_conditions.element_to_be_clickable(locator))

  def wait_until_element_should_not_be_visible(self, locator, seconds):
    self.wait = self.web_driver_wait(seconds)
    self.wait.until_not(expected_conditions.presence_of_element_located(locator))

  def is_element_enabled(self, locator):
    return self.get_webelement(locator).is_enabled()


  