check: lint test

install:
	poetry install --no-interaction
	poetry run pre-commit install

lint:
	poetry run pflake8 snippets_python/
	poetry run isort --check --diff snippets_python/
	poetry run black --check snippets_python/

format:
	poetry run isort snippets_python/
	poetry run black snippets_python/

test:
	poetry run pytest -vv --cov=snippets_python/ --cov-report=term-missing
