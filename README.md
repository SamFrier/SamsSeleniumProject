# Selenium-Grid: A Beginner's Guide

### By Sam Frier

## Introduction

Selenium is, in general, a framework designed to automate web browser activity; however its primary use is to provide automated testing for web applications. It includes a scripting language (Selenese) that allows users to write tests for various different programming languages, including Ruby, Python and Java. Alternatively, users can write tests in an IDE instead of via a script. When run, Selenium creates an instance of a specified web browser (real or virtual) and runs the tests inside it.

Selenium-Grid allows users to run tests on browser instances that are running on a remote server. One or more browser instances (or *nodes*) connect to a central *hub*, and tests can use these instances by accessing the hub. This way, tests can be run across multiple machines.

When developing a web application, Selenium-Grid can be incorporated into the DevOps pipeline wherever testing is required: specifically, it can be linked to CI servers such as Jenkins or build tools such as Maven in order to run automated tests whenever a build is triggered. To enable this, we must first set up a Selenium-Grid server.

## Installation Guide

...

## Usage Guide

...

## Sources

http://www.seleniumhq.org/docs/07_selenium_grid.jsp
https://linuxmeerkat.wordpress.com/2014/10/17/running-a-gui-application-in-a-docker-container/
https://www.gridlastic.com/python-code-example.html 

