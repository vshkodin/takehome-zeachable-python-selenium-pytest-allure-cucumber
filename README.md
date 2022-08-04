### Example of UI Testing Framework using Python, Pytest, Pytest-BDD, and Selenium.

[Test plan](https://docs.google.com/document/d/1yU7LNGNEMCRSPuB21Mb32SgAE_WPklTZ4qouoAUmvd8/edit?usp=sharing)

[Load/Performance test results](https://docs.google.com/document/d/1queAzmeWT_8DiEDIP_3EF5jcR_qgWpUf_8R7DeOV1JI/edit?usp=sharing)


https://takehome.zeachable.com/

### How to Build/Run locally:
#### clone repo:
```
git clone https://github.com/vshkodin/takehome-zeachable-python-selenium-pytest-allure-cucumber.git
cd takehome-zeachable-python-selenium-pytest-allure-cucumber
```
#### Dependencies 
1. In order to run you have to install Python3.6+
2. You need to have pip installed
3. install python3 - pip  https://www.python.org/downloads/
7. Getting dependencies:
```
$ pip install virtualenv
$ python3 virtualenv env
$ env/Scripss/activate (for win)
$ source env/bin/activate (for mac-linux)
$ pip install -r requirements.txt
$ brew install allure
```

#### Running  tests

![alt text](SeleniumResults.png)

![alt text](SeleniumAllureResults.png)


* Headful is default run
```
pytest 
```
* in order to run Headless 
```
pytest --headless true
```
* See report 
```commandline
allure serve allure-report
```



### API tests Using Postman Newman
* CLI report for API
![alt text](NewmanPostman.png)

* Allure report for API
![alt text](allure-report-API.png)

* HOW to run
```
npm install -g newman
npm install -g newman-reporter-allure
newman run  --verbose https---takehome.zeachable.com-.postman_collection.json -r allure --reporter-allure-export allure-report/
```


### VRT tests using BackstopJS

* BackstopJS report
![alt text](backstopJSReport.png)


* HOW to run
```commandline
 npm install -g backstopjs
 backstop test
```
