ISORT="venv/bin/isort"
PIP="venv/bin/pip"
TOX="venv/bin/tox"

TMP_PIP="venv_tmp/bin/pip"

REQUIREMENTS_BASE:=requirements/base.txt
REQUIREMENTS_TEST:=requirements/test.txt

.PHONY: requirements

requirements:
	virtualenv -p python3.6 venv_tmp
	$(TMP_PIP) install -U "pip"
	$(TMP_PIP) install -r $(REQUIREMENTS_BASE)
	$(TMP_PIP) freeze > requirements/requirements.txt
	@rm -rf venv_tmp

virtualenv:
	test -d venv || virtualenv -p python3.6 venv
	$(PIP) install -U "pip"
	$(PIP) install -r $(REQUIREMENTS_TEST)

test: virtualenv
	$(TOX)

isort: virtualenv
	$(ISORT) -rc -y djtools/
