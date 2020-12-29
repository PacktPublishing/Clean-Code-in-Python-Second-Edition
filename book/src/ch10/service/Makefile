LISTEN_HOST:="127.0.0.1"
LISTEN_PORT:=8080
DBHOST:="127.0.0.1"
DBPORT:=5432

.PHONY: clean
clean:
	find . -type d -name __pycache__ | xargs rm -fr {}
	find . -type d -name "*.egg-info" | xargs rm -fr {}

.PHONY: build
build:
	docker-compose build

.PHONY: run
run:
	docker-compose run --service-ports -d web

.PHONY: typehint
typehint:
	mypy --ignore-missing-imports libs/web
	mypy --ignore-missing-imports libs/storage
	mypy --ignore-missing-imports statusweb

.PHONY: lint
lint:
	black --check --line-length=79 libs statusweb

.PHONY: format
format:
	black --line-length=79 libs statusweb

.PHONY: build-deps
build-deps:
	$(MAKE) -C libs/web build
	$(MAKE) -C libs/storage build
