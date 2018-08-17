TEST_PIP="venv_test/bin/pip"
TEST_TOX="venv_test/bin/tox"

test:
	test -d venv_test || virtualenv -p python3.6 venv_test
	$(TEST_PIP) install -U "pip"
	$(TEST_PIP) install tox
	$(TEST_TOX)
