export PYTHONPATH=src
VIRTUAL_ENV ?= /usr/local
PYTHON:=$(VIRTUAL_ENV)/bin/python

.PHONY: clean
clean:
	find . -name "*.swp" -o -name "__pycache__" | xargs rm -fr

.PHONY: test
test: lint typehint
	@$(PYTHON) -m doctest src/*.py
	pytest tests $(ARGS)

.PHONY: typehint
typehint:
	@mypy src/*.py

.PHONY: lint
lint:
	black --check --line-length=79 src tests

.PHONY: format
format:
	black --line-length=79 src tests
