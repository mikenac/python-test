init:
	pip install -r requirements.txt

lint:
	pylint -j 4 src/*.py

test: lint
	nosetests --with-xcoverage --cover-erase

.PHONY: init test

 