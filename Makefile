build: ; \
    virtualenv -p python3.4 env; \
    ./env/bin/pip install --download-cache /tmp/pip -r requirements.txt

clean: ; \
    rm -fr env; \
    rm -f `find . -name *.pyc`; \
    rm -f perfreports/static/charts/*.png

flake8: ; \
    ./env/bin/flake8 --max-line-length=80 perfreports

test: flake8;
