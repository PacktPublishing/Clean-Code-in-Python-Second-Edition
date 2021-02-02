PYTHON=python3.9
ENV_NAME=.env
DOCKER_VERSION:=latest

.PHONY: clean
clean:
	find . -name "*.swp" -o -name "__pycache__" -o -name ".mypy_cache" | xargs rm -fr
	rm -fr $(ENV_NAME)

.PHONY: setup
setup:
	$(PYTHON) -m venv $(ENV_NAME)
	$(ENV_NAME)/bin/python -m pip install -r requirements.txt

.PHONY: shell
shell:
	docker run -it rmariano/ccip:$(DOCKER_VERSION)

.PHONY:	test
test:
	for chapter_dir in $(shell ls -d ch0*); do \
		echo "Testing $$chapter_dir"; \
		$(MAKE) test -C $$chapter_dir ; \
	done
