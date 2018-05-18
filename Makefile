MODULE_PATH=json_message_processor

init: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -r requirements.txt
	touch venv/bin/activate

lint:
	@. venv/bin/activate; pylint -j 4 ${MODULE_PATH}/*.py

test: init lint
		@. venv/bin/activate; \
		coverage run --branch -m unittest discover -s tests/; 
		@. venv/bin/activate; \
		coverage report --omit "*__init__*" -m ${MODULE_PATH}/*.py; 
clean:
	@rm -rf venv
	@find . -name "*.pyc" -delete
	@rm .coverage

ci_init:
	pip install -r requirements.txt

ci:
	pylint -j 4 ${MODULE_PATH}/*.py
	coverage run --branch -m unittest discover -s tests/
	coverage report --omit "*__init__*" -m ${MODULE_PATH}/*.py

.PHONY: init test lint ci ci_init

 