PYTEST := uv run pytest
COV_OPTS := --cov=winix_api --cov-report=xml:coverage.xml --cov-report=term
TEST_PATH := tests/
ACTIVATE := source .venv/bin/activate;

.PHONY: test coverage clean

test:
	$(ACTIVATE) $(PYTEST) $(COV_OPTS) --maxfail=1 --disable-warnings $(TEST_PATH)

coverage:
	$(ACTIVATE) $(PYTEST) $(COV_OPTS) $(TEST_PATH)

clean:
	rm -f coverage.xml
	rm -rf .pytest_cache .coverage
