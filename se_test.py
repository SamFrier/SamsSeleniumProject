from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#os.environ["webdriver.gecko.driver"] = ""

driver = webdriver.Remote(
  command_executor = "http://localhost:4444/wd/hub",
  desired_capabilities = {
    "browserName": "firefox",
    #"version": "47",
    #"video": "False",
    "platform": "LINUX",
    "marionette": "false",
  }
)

#print ("Video: " + VIDEO_URL + driver.session_id)

try:
  driver.implicitly_wait(30)
  driver.get("http://www.python.org")
  assert "Python" in driver.title
finally:
  driver.quit()
