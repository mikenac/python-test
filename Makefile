VIRTUALENV = virtualenv --python=python3
VENV := $(if $(VIRTUAL_ENV),$(VIRTUAL_ENV),.venv)
PYTHON = $(VENV)/bin/python
REQ_STAMP = $(VENV)/.req_stamp

# editable
MODULE_PATH=json_message_processor

virtualenv: $(PYTHON)

$(PYTHON):
	@$(VIRTUALENV) $(VENV)

init: virtualenv $(REQ_STAMP)

$(REQ_STAMP): requirements.txt
	@$(VENV)/bin/pip install -Ur requirements.txt
	@touch $(REQ_STAMP)

lint:
	@$(VENV)/bin/pylint -j 4 ${MODULE_PATH}/*.py

test: init lint
		@$(VENV)/bin/coverage run --branch -m unittest discover -s tests/
		@$(VENV)/bin/coverage report --omit "*__init__*" -m ${MODULE_PATH}/*.py

clean:
	@rm -rf $(VENV)
	@find . -name "*.pyc" -delete
	@rm .coverage

.PHONY: init test lint

 