
init: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate
lint:
	. venv/bin/activate; pylint -j 4 src/*.py

test: init lint
		. venv/bin/activate; \
		python -m unittest discover -s test -p *.py; \
		coverage report -m src/*.py; 
clean:
	rm -rf venv
	find . -name "*.pyc" -delete

.PHONY: init test lint

 