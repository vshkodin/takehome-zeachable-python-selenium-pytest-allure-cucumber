# UI selenium

ui-test:
	pytest

ui-test-headless:
	pytest --headless true

ui-report:
	allure serve allure-report


# API

api-build-local:
	npm install -g newman && npm install -g newman-reporter-allure

api-test:
	newman run  --verbose https---takehome.zeachable.com-.postman_collection.json -r allure --reporter-allure-export allure-report/


api-report:
	allure serve allure-report

# VRT

vrt-build:
	npm install -g backstopjs

vrt-test:
	backstop test

vrt-approve:
	backstop approve

vrt-report:
	backstop approve


# EXTRA

clean:
	rm -rf allure-report/