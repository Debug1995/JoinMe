# JoinMe is the final project of the Advanced Software Engineering course at Columbia University.
This Readme file contains step by step instructions on how to build, test, install and operate our application.

# How to Install
Before using our JoinMe platform, you need to install some python packages to make our platform able to run under your pc environment.

For the frontend of our platform, we mainly used the PyQt5 framework.
To install the PyQt5, you only need to run the following code in your terminal：
pip install PyQt5
What’s more, we also need the mysql-connector package to make our platform able to communicate with our database. To do so, you need to install the package using the following code:
pip install mysql-connector
Since our platform embedded the Google Map, Gmail, and AWS service as well. In order to power these services, you need to install some packages by running the following code in your terminal.
For Gmail:
pip install --upgrade google-api-python-client oauth2client
pip install email
pip install pybase64
For Google Map:
pip install googlemaps
For AWS:
pip install boto3
Furthermore, we also use some supposed-built-in python package in our platform. They should have been originally built with the python. But if you find any of them are not stalled in your environment, please just run the following code in your terminal.
pip install ast
pip install datetime
pip install threading
pip install time
pip install urllib.request
pip install webbrowser
You have installed all the needed packages for launching our platform. 
Just have fun!

# How to Test
The test of our application could be separated into three parts, unit test, branch coverage test and static analysis. All test reports are stored in the ./report.

Unit test: 
To do unit test, install the unittest library using:
pip install unittest
And run the file of unit_test.py under the main directory of our project, then a new unit test report will generate and be attached at the end of our unittest_log.txt file.

Branch coverage test:
To do branch coverage test, install the coverage library using:
pip install coverage
Then to measure the branch coverage of my test unit, using the command
coverage run unit_test.py
After that, the report can be extracted by using either
coverage report
Which will print the report on the terminal windows, Or using 
coverage html
Which will generate annotated HTML listings with coverage results. The HTML report will be generated under the main directory by default, or using -d argument to specify an output directory. In our project, we use:
coverage html -d ./report/branch_coverage_report
To store the HTML under the ./report as a single file branch_coverage_report

Static analysis:
To do static analysis, install static analysis tool pylint:
pip install pylint
Implement pylint on different python files to generate specific static analysis report on the terminal screen. The basic command is:
pylint xxx.py
