# UI selenium

ui-test:
	pytest

ui-test-headless:
	pytest --headless true

ui-report:
	allure serve allure-report

ui-docker-build:
	docker build -f Dockerfile.python-pytest . -t pytest:latest

ui-docker-test:
	docker network create web && docker-compose up --remove-orphans --exit-code-from test-framework && docker-compose down && docker network rm web

# API

api-build-local:
	npm install -g newman && npm install -g newman-reporter-allure

api-test:
	newman run  --verbose https---takehome.zeachable.com-.postman_collection.json -r allure --reporter-allure-export allure-report/

api-report:
	allure serve allure-report

api-docker-build:
	docker build -t api:latest -f Dockerfile.api .

api-docker-run:
		docker run --rm --mount type=bind api:latest https---takehome.zeachable.com-.postman_collection.json


# VRT

vrt-build:
	npm install -g backstopjs

vrt-test:
	backstop test

vrt-approve:
	backstop approve

vrt-report:
	backstop approve

vrt-docker-build:
	docker build -t vrt:latest -f Dockerfile.vrt .

vrt-docker-run:
		docker run --rm --mount type=bind vrt:latest test

vrt-docker-approve:
		docker run --rm --mount type=bind vrt:latest approve

# EXTRA

clean:
	rm -rf allure-report/ && rm -rf backstop_data/bitmaps_test