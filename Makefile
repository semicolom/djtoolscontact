ISORT="venv/bin/isort"
PIP="venv/bin/pip"

TEST_PIP="venv_test/bin/pip"
TEST_TOX="venv_test/bin/tox"

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

test:
	test -d venv_test || virtualenv -p python3.6 venv_test
	$(TEST_PIP) install -U "pip"
	$(TEST_PIP) install tox
	$(TEST_TOX)

isort: virtualenv
	$(ISORT) -rc -y djtools/
