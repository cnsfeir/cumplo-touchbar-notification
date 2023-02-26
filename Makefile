# Install Poetry
.PHONY: get-poetry
get-poetry:
	curl -sSL https://install.python-poetry.org | python3 - --version 1.3.2
	export PATH="$(HOME)/.poetry/bin:$(PATH)"

# Build virtual environment and install dependencies
.PHONY: build-venv
build-venv:
	poetry config virtualenvs.in-project true
	poetry install
