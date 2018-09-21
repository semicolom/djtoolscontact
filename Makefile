PIP="venv/bin/pip"
TOX="venv/bin/tox"

clean:
	@find . -name *.pyc -delete
	@rm -rf venv

virtualenv:
	test -d venv || virtualenv -p python3.6 venv
	$(PIP) install -U "pip"

test: virtualenv
	$(PIP) install -U "tox"
	$(TOX)
