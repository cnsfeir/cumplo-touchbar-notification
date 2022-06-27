# Default values
POETRY_VERSION = 1.1.13
PYTHON_VERSION = 3.10

# Imports .env variables
ENV	:= $(PWD)/.env
include $(ENV)

# Sets Python version at pyproject.py
.PHONY: py-version
py-version:
	mv pyproject.toml temp_pyproject.toml
	sed 's/PYTHON_VERSION/$(PYTHON_VERSION)/' temp_pyproject.toml > pyproject.toml
	rm temp_pyproject.toml

# Install Poetry
.PHONY: get-poetry
get-poetry:
	curl -sSL https://install.python-poetry.org | python3 - --version $(POETRY_VERSION)
	export PATH="$(HOME)/.poetry/bin:$(PATH)"

# Build virtual environment and install dependencies
.PHONY: build-venv
build-venv:
	make py-version
	poetry config virtualenvs.in-project true
	poetry install
	poetry run pre-commit install

# Runs pre-commit inside poetry virtual environment
.PHONY: pre-commit
pre-commit:
	poetry run pre-commit

# Run tests
.PHONY: tests
tests:
	poetry run pytest
