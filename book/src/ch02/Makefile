PYTHON:=$(VIRTUAL_ENV)/bin/python
export PYTHONPATH=src

.PHONY: test
test:
	@$(PYTHON) -m doctest tests/*.py
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
	find . -type d -name __pycache__ | xargs rm -fr {}
