PYTHON=python3.8
ENV_NAME=.env

clean:
	find . -name "*.swp" -o -name "__pycache__" | xargs rm -fr
	rm -fr $(ENV_NAME)

setup:
	$(PYTHON) -m venv $(ENV_NAME)
	$(ENV_NAME)/bin/python -m pip install -r requirements.txt

.PHONY: clean setup
