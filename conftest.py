import pytest
from selenium import webdriver

def pytest_addoption(parser):
  parser.addoption("--browser_name", action="store", default="firefox")

@pytest.fixture(scope="class")
def setup_teardown(request):
  driver = ""
  browser_name = request.config.getoption("--browser_name")
  if(browser_name == "firefox"):
    driver = webdriver.Firefox()
  elif(browser_name == "chrome"):
    driver = webdriver.Chrome()
  driver.maximize_window()
  driver.implicitly_wait(15)
  request.cls.driver = driver
  yield
  driver.quit()
