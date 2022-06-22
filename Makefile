POETRY_VERSION = 1.1.13

# Install Poetry
.PHONY: get-poetry
get-poetry:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 - --version $(POETRY_VERSION)

# Build virtual environment and install dependencies
.PHONY: build-venv
build-venv:
	poetry config virtualenvs.in-project true
	poetry install

# Run tests
.PHONY: tests
tests:
	poetry run pytest
