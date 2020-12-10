COMPILED_HTML := compiled_html

test:
	$(VIRTUAL_ENV)/bin/py.test --cov-report term-missing --cov=. test.py

setup:
	$(VIRTUAL_ENV)/bin/pip install -r requirements.txt

# use: highlight SOURCE=<SOURCE>
highlight:
	mkdir -p $(COMPILED_HTML)
	$(VIRTUAL_ENV)/bin/pygmentize \
		-f html \
		-l python3 \
		-O full,style=colorful \
		$(SOURCE) > $(COMPILED_HTML)/$(SOURCE).html

.PHONY: test setup highlight
