
init: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate
lint:
	. venv/bin/activate; pylint -j 4 src/*.py

test: lint
		. venv/bin/activate; \
		python -m unittest discover -s test -p *.py; \
		coverage report -m src/*.py; \

.PHONY: init test lint

 