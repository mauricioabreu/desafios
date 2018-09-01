.PHONY: deps test

.DEFAULT_GOAL := test

# Install dependencies
deps:
	pip install lxml requests pytest python-telegram-bot

# Run test suite
test:
	py.test tests
