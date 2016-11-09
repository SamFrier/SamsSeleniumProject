# Selenium-Grid: A Beginner's Guide

### By Sam Frier

## Introduction

Selenium is, in general, a framework designed to automate web browser activity; however its primary use is to provide automated testing for web applications. It includes a scripting language (Selenese) that allows users to write tests for various different programming languages, including Ruby, Python and Java. Alternatively, users can write tests in an IDE instead of via a script. When run, Selenium creates an instance of a specified web browser (real or virtual) and runs the tests inside it.

Selenium-Grid allows users to run tests on browser instances that are running on a remote server. One or more browser instances (or *nodes*) connect to a central *hub*, and tests can use these instances by accessing the hub. This way, tests can be run across multiple machines.

When developing a web application, Selenium-Grid can be incorporated into the DevOps pipeline wherever testing is required: specifically, it can be linked to CI servers such as Jenkins or build tools such as Maven in order to run automated tests whenever a build is triggered. To enable this, we must first set up a Selenium-Grid server.

## Installation Guide

...

## Usage Guide

By connecting to the Selenium-Grid, we can run automated tests in a variety of languages, and these tests can be automated further by including them as part of e.g. a Maven build.

For example, let’s define a very simple test in Python. First we must download the Selenium module for Python:

`pip install selenium`

From here, we can write the following script to test the title of a web page:

`\# filename: se_test.py

from selenium import webdriver

driver = webdriver.Remote(
command_executor = "http://<hub_ip>:4444/wd/hub", # add your hub’s IP address here
  desired_capabilities = {
    "browserName": "firefox",
  }
)

try:
  driver.implicitly_wait(30)
  driver.get("http://www.python.org")
  print(driver.title)
  assert "Python" in driver.title
finally:
  driver.quit()
When we run this script, Python will create a driver that connects to the Selenium-Grid hub and requests a Firefox browser. The hub will then register a Firefox instance on one of the nodes to this driver. The driver then sends a request for the specified URL to the node, which opens the page in Firefox and sends the contents back to the driver. Finally, we can check the page’s title and test if it is what we were expecting.
~$ python se_test.py
Welcome to Python.org`

(Since the unit test was successful, it will not produce any output.)

## Sources

http://www.seleniumhq.org/docs/07_selenium_grid.jsp

https://linuxmeerkat.wordpress.com/2014/10/17/running-a-gui-application-in-a-docker-container/

https://www.gridlastic.com/python-code-example.html 

