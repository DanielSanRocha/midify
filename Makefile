help: ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

setup: ## Install requirements
	@pip install -r requirements.txt
	@pip install -r requirements.dev.txt

build: ## Build the project
	@python setup.py sdist

upload: clean build ## Uplad to PyPi
	@twine upload dist/*

test: ## Run unit/integration tests
	@PYTHONPATH=. pytest tests -s -p no:warnings

clean: ## Cleans the directory
	@rm -rf dist
	@rm -rf midify/__pycache__
	@rm -rf tests/__pycache__
	@rm -rf .pytest_cache
	@rm -rf output.mid
	@rm -rf notebooks/.ipynb_checkpoints
	@rm -rf MANIFEST
