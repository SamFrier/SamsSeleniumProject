# Selenium-Grid: A Beginner's Guide

## Introduction

Selenium is, in general, a framework designed to automate web browser activity; however its primary use is to provide automated testing for web applications. It includes a scripting language (Selenese) that allows users to write tests for various different programming languages, including Ruby, Python and Java. Alternatively, users can write tests in an IDE instead of via a script. When run, Selenium creates an instance of a specified web browser (real or virtual) and runs the tests inside it.

Selenium-Grid allows users to run tests on browser instances that are running on a remote server. One or more browser instances (or *nodes*) connect to a central *hub*, and tests can use these instances by accessing the hub. This way, tests can be run across multiple machines.

When developing a web application, Selenium-Grid can be incorporated into the DevOps pipeline wherever testing is required: specifically, it can be linked to CI servers such as Jenkins or build tools such as Maven in order to run automated tests whenever a build is triggered. To enable this, we must first set up a Selenium-Grid server.

## Installation Guide

This guide will focus on installing Selenium-Grid on a machine running Ubuntu 16.04, however the process is similar for other operating systems. Selenium-Grid requires Java 8 or higher on both the hub and nodes.

1.	Download the Selenium Server jar file from this link: https://goo.gl/Lyo36k
	
	Alternatively, download the file via the command line:
	
	    ~$ wget –O selenium-server-standalone.jar https://goo.gl/Lyo36k
	
2.	Start a hub using the following command: 

	    ~$ java -jar selenium-server-standalone.jar -role hub
	
	If you want to use this machine while the hub is running, specify that the process should run in the background by adding a `&` to the end of the command.
	
3.	For the Selenium node(s), download the jar file as above. (We will be using a different set of flags when running it on a node, which will be given later.)

4.	In order for the nodes to run tests, you will need to make sure the browser(s) you want to test on are installed on the node machine. For example, in order to set up Firefox on a node:

	*	Install the browser itself via e.g. `apt-get`.
	
	*	Install the geckodriver for Firefox (this is required for Selenium Server 3.0 and later), which requires its own set of steps:

		*	Download the geckodriver tarball using e.g. `wget` from here: https://github.com/mozilla/geckodriver
		
		*	Unpack the tarball into a directory of your choice.
		*	Add this directory to your path:
		
			    ~$ export PATH=$PATH:/path/to/geckodriver
		      
		*	Depending on the environment in which your node is running (e.g. a Docker container), you may want to run the browser in headless mode. In Ubuntu, this can be done via the following method:
		
		*	Install Xvfb using the command `apt-get install -y xvfb`.
		
		*	Set the `DISPLAY` environment variable to something other than `:0`:
		
			    ~$ export DISPLAY=:1
			    
		*	Run Xvfb as a background process using the display you specified:
		
			    ~$ Xvfb :1 &
			    
5.	Finally, start the nodes via this command:

	    ~$ java -jar selenium-server-standalone.jar -role node –hub http://<hub_ip>:4444/grid/register
	    
	where `<hub_ip>` is the IP address of your hub (or `localhost` if running the node on the same machine as the hub). We can also use the `-browser` flag to specify what browser instances we want to run on the node (this flag can be used multiple times if desired):
	
	    ~$ java -jar selenium-server-standalone.jar -role node –hub http://<hub_ip>:4444/grid/register -browser browserName=firefox,maxInstances=5
	
Once the hub and node(s) are set up, visit `http://<server_ip>:4444/grid/console` to view the grid.


## Usage Guide

By connecting to the Selenium-Grid, we can run automated tests in a variety of languages, and these tests can be automated further by including them as part of e.g. a Maven build.

For example, let’s define a very simple test in Python. First we must download the Selenium module for Python:

```
~$ pip install selenium
```

From here, we can write the following script to test the title of a web page:

``` Python
# filename: se_test.py

from selenium import webdriver

driver = webdriver.Remote(
command_executor = "http://<hub_ip>:4444/wd/hub", # add your hub’s IP address here
  desired_capabilities = {
    "browserName": "firefox",
  }
)

try:
  driver.implicitly_wait(30) 		# timeout of 30s when looking for an element
  driver.get("http://www.python.org")
  print(driver.title)
  assert "Python" in driver.title
finally:
  driver.quit()
```

When we run this script, Python will create a driver that connects to the Selenium-Grid hub and requests a Firefox browser. The hub will then register a Firefox instance on one of the nodes to this driver. The driver then sends a request for the specified URL to the node, which opens the page in Firefox and sends the contents back to the driver. Finally, we can check the page’s title and test if it is what we were expecting.

```
~$ python se_test.py
Welcome to Python.org
```

(Since the unit test was successful, it will not produce any output.)

## Sources

http://www.seleniumhq.org/docs/07_selenium_grid.jsp

https://linuxmeerkat.wordpress.com/2014/10/17/running-a-gui-application-in-a-docker-container/

https://www.gridlastic.com/python-code-example.html 

