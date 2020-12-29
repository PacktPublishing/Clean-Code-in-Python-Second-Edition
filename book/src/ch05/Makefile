VIRTUAL_ENV ?= /usr/local
PYTHON:=$(VIRTUAL_ENV)/bin/python
export PYTHONPATH=src

.PHONY: test
test:
	@$(PYTHON) -m doctest tests/*.py
	@$(PYTHON) -m unittest tests/*.py

.PHONY: typehint
typehint:
	mypy src tests

.PHONY: checklist
checklist: lint typehint test

.PHONY: lint
lint:
	black --check --line-length=79 \
		--exclude src/pep0614.py \
		src tests

.PHONY: format
format:
	black --line-length=79 \
		--exclude src/pep0614.py \
		src tests

.PHONY: clean
clean:
	find . -name "*.swp" -o -name "__pycache__" | xargs rm -fr
