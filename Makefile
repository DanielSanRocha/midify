help: ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

setup: ## Install requirements
	@pip install -r requirements.txt
	@pip install -r requirements.dev.txt

build: ## Build the project
	@python setup.py sdist

upload: clean build ## Uplad to PyPi
	@twine upload dist/*

test: ## Run unit tests
	@PYTHONPATH=. pytest tests

clean: ## Cleans the directory
	@rm -rf dist
