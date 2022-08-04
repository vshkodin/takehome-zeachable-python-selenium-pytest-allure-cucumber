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
```

#### Running  tests
* Headful is default run
```
pytest 
```
* in order to run Headless 
```
pytest --headless true
```

### API tests Using Postman Newman

```
npm install -g newman
newman run  --verbose https---takehome.zeachable.com-.postman_collection.json
```

### VRT tests using BackstopJS
