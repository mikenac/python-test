init:
	pip install -r requirements.txt

test:
	nosetests --with-xcoverage --cover-erase

.PHONY: init test

