MODULE_PATH=json_message_processor

init: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate

lint:
	@. venv/bin/activate; pylint -j 4 ${MODULE_PATH}/*.py

test: init lint
		@. venv/bin/activate; \
		coverage run --branch -m unittest discover -s tests -p *.py; \
		coverage report --omit "*__init__*" -m ${MODULE_PATH}/*.py; 
clean:
	@rm -rf venv
	@find . -name "*.pyc" -delete
	@rm .coverage

.PHONY: init test lint

 