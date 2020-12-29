export PYTHONPATH=src
PYTHON:=$(VIRTUAL_ENV)/bin/python

.PHONY: test
test:
	@$(PYTHON) -m doctest src/*.py
	@$(PYTHON) -m unittest tests/*.py

.PHONY: typehint
typehint:
	mypy src tests

.PHONY: lint
lint:
	black --check --line-length=79 src tests

.PHONY: format
format:
	black --line-length=79 src tests

.PHONY: clean
clean:
	find . -name "*.swp" -o -name "__pycache__" | xargs rm -fr
