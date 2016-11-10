from selenium import webdriver

driver = webdriver.Remote(
  command_executor = "http://localhost:4444/wd/hub",
  desired_capabilities = {
    "browserName": "chrome",
    #"platform": "LINUX",
  }
)

try:
  driver.implicitly_wait(30)
  driver.get("http://www.python.org")
  print(driver.title)
  assert "Python" in driver.title
finally:
  driver.quit()
