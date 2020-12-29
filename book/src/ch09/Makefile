VIRTUAL_ENV ?= /usr/local
PYTHON:=$(VIRTUAL_ENV)/bin/python
export PYTHONPATH=src

.PHONY: test
test:
	@$(PYTHON) -m doctest src/*.py
	@$(PYTHON) -m unittest tests/*.py

.PHONY: clean
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name __pycache__ | xargs rm -fr {}

.PHONY: typehint
typehint:
	@mypy src/*.py

.PHONY: lint
lint:
	black --check --line-length=79 src tests

.PHONY: format
format:
	black --line-length=79 src tests

.PHONY: checklist
checklist: lint typehint test
