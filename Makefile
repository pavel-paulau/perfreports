ENV = env
ENV_BIN = $(ENV)/bin

PIP_CACHE = /tmp/pip


build:
	virtualenv $(ENV)
	$(ENV_BIN)/pip install --download-cache $(PIP_CACHE) -r requirements.txt

clean:
	rm -fr env
	rm -f `find . -name *.pyc`
	rm -f perfreports/static/charts/*.png

flake8:
	$(ENV_BIN)/flake8 --max-line-length 80 --exclude perfreports/__init__.py perfreports

test: flake8

run:
	$(ENV_BIN)/python runserver.py
