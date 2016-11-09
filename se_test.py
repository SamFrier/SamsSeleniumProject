from selenium import webdriver

driver = webdriver.Remote(
  command_executor = "http://52.210.77.132:4444/wd/hub",
  desired_capabilities = {
    "browserName": "firefox",
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
