PYTHON=python3.8

.PHONY: typehint
typehint:
	mypy --ignore-missing-imports src/

.PHONY: test
test:
	pytest tests/

.PHONY: lint
lint:
	pylint src/

.PHONY: checklist
checklist: lint typehint test

.PHONY: black
black:
	black -l 79 *.py

.PHONY: setup
setup:
	$(VIRTUAL_ENV)/bin/pip install -r requirements.txt

.PHONY: clean
clean:
	find . -type f -name "*.pyc" | xargs rm -fr
	find . -type d -name __pycache__ | xargs rm -fr
