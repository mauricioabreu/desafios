.PHONY: deps test

.DEFAULT_GOAL := test

# Install dependencies
deps:
	pip install lxml requests pytest

# Run test suite
test:
	py.test tests
