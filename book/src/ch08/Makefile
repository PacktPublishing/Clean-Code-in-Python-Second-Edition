CASE:=1
VIRTUAL_ENV ?= /usr/local
PYTHON:=$(VIRTUAL_ENV)/bin/python
export PYTHONPATH=src

.PHONY: test
test:
	@$(PYTHON) -m doctest src/*.py
	@$(VIRTUAL_ENV)/bin/pytest tests/

.PHONY: clean
clean:
	find . -type d -name __pycache__ | xargs rm -fr {}
	rm -fr .coverage .pytest_cache/ .hypothesis/

.PHONY: coverage
coverage:
	bash run-coverage.sh

.PHONY: mutation
mutation:
	@bash mutation-testing.sh $(CASE)

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
