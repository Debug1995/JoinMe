### JoinMe is the final project of the Advanced Software Engineering course at Columbia University.
This Readme file contains step by step instructions on how to build, test, install and operate our application.

* [Install and Build](#how-to-install-and-build)
* [Test](#how-to-test)
* [Operate](#how-to-operate)

## How to Install and Build
Before using our JoinMe platform, you need to install some python packages to make our platform able to run under your pc environment.

For the frontend of our platform, we mainly used the PyQt5 framework.
To install the PyQt5, you only need to run the following code in your terminal：
```shell
pip install PyQt5
```
What’s more, we also need the mysql-connector package to make our platform able to communicate with our database. To do so, you need to install the package using the following code:
```shell
pip install mysql-connector
```
Since our platform embedded the Google Map, Gmail, and AWS service as well. In order to power these services, you need to install some packages by running the following code in your terminal.

For Gmail:
```shell
pip install --upgrade google-api-python-client oauth2client
pip install email
pip install pybase64
```
For Google Map:
```shell
pip install googlemaps
```
For AWS:
```shell
pip install boto3
```
Furthermore, we also use some supposed-built-in python package in our platform. They should have been originally built with the python. But if you find any of them are not stalled in your environment, please just run the following code in your terminal.
```shell
pip install ast
pip install datetime
pip install threading
pip install time
pip install urllib.request
pip install webbrowser
```
You have installed all the needed packages for launching our platform. 
Just have fun!

## How to Test
The test of our application could be separated into three parts, unit test, branch coverage test and static analysis. All test reports are stored in the ./report.
### Unit test: 
To do unit test, install the unittest library using:
```shell
pip install unittest
```
And run the file of unit_test.py under the main directory of our project, then a new unit test report will generate and be attached at the end of our unittest_log.txt file.
### Branch coverage test:
To do branch coverage test, install the coverage library using:
```shell
pip install coverage
```
Then to measure the branch coverage of my test unit, using the command
```shell
coverage run unit_test.py
```
After that, the report can be extracted by using either
```shell
coverage report
```
Which will print the report on the terminal windows, Or using 
```shell
coverage html
```
Which will generate annotated HTML listings with coverage results. The HTML report will be generated under the main directory by default, or using -d argument to specify an output directory. In our project, we use:
```shell
coverage html -d ./report/branch_coverage_report
```
To store the HTML under the ./report as a single file branch_coverage_report
### Static analysis:
To do static analysis, install static analysis tool pylint:
```shell
pip install pylint
```
Implement pylint on different python files to generate specific static analysis report on the terminal screen. The basic command is:
```shell
pylint xxx.py
```
## How to Operate
### Signing in and Signing up
Before using our application, each user needs to acquire a google account. After launching the product, you will be shown the login page. Simply click on the “Sign In with Google” button. The browser will open up a web page where you are prompted to select one of your Google accounts to proceed. Beware that the email address associated with that account will serve as your contact information for outgoing messages. Enter your password and consent on the application’s usage of your account as instructed by the website. Finally, you will reach a page where you will be provided with a token. Copy this token, and paste it back to the input box now appears on the application. Close your browser. 

At this point, if you have previously registered with our application, you will be immediately logged in. If not, you will be shown a signup page where you will enter your personal information. Please note that you can only register if you enter valid information. If you enter information like invalid date of birth or non-existent address, the application will send you a warning on correcting the mistakes. You can also upload images from your local directory as your profile picture. Simply click “Upload” and choose a file from the dialog that follows. A preview will be displayed once the upload completes. When you are done entering the information, hit “Sign Up” to save your profile. You will be shown back to the sign in page. Proceed as you have a account now, and you will reach our main page. 
### Hosting Events
If you want to host a new event, click on the “Host Event” button on the top left corner of the main page. In the following window, enter the title, description, category, date, duration, and location of the event. As is with signing up, the system will check and inform you if any of the information is invalid. You can also upload three descriptive images by clicking the three “Upload” buttons at the bottom of the pagPreviews will be displayed. Hit “Save” when you are ready to post event. You will be able to preview the event in the next page. Hit “Edit” if you want to re-edit the event. Press “Back” to post the event to our system. You will go back to the main page. 

Your can see three events that you have posted in the “Hosted” panel on the main page. Click on the number on the panel to view the events as mention in the last paragraph. You still have the option to re-edit the event by hitting “Edit” on the page. Press back to finish the review. 

In addition to editing information as you did in posting the event, you can now manage the attendees. In the event review page. You can contact your attendees by sending them emails. Enter the message you would like to send in the message box. Enter a user’s nickname if you want to contact that person privately. Otherwise, just hit the “Send Button” to send to every attendee. Emails will be sent from your gmail account that you signed up with. You can also remove attendees in the event editing page. Hover your mouse over the profile image of the attendee that you would like to remove until a red cross appear across it. Click on the image to remove the user. Hit save to return to the event review page.  
### Finding and Joining Events
To join events, you will have to search for them first. By default, you will be shown events that is in the same state with the same tag that you entered in your profile on the lists on the left hand side. You can flip pages by pressing the left and right arrow. You can configure the filter of events by selecting the tag, state, time and keyword of the event. Press “Search” to search for events. If you do not specify an option, all events will be shown. Click on the title of the event to view the event. 

In the event view page, you can see all the details of the event. Click on the pin button on the bottom right corner to view the location of the event in the browser. Enter message in the message and press “Contact Host” to send the host of the event a message via email. When you are ready to join the event, press on “Join”. 

You can view the event you have joined in the “Attend” panel. Click on the number to view the event. You can also click on “See More” to view a complete list of joined events on the left-side list. 
### Others
You can edit your profile by clicking on the “Update Profile” button on the main page. Modify the information you would like to change and press save to update the profile. Press “Log Out” to quit the application. You can then login with another account. 

You have to maintain network throughout the usage of the application as it communicates with a remote database constantly.
