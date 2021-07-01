PY=python3
TESTS=tests/test_load_modules.py
MAIN=jarvis.py

.PHONY: run test

run:
	$(PY) $(MAIN)

test:
	pytest $(TESTS)

