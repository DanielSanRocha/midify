help: ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

build: ## Build the project
	@python setup.py sdist

upload: ## Uplad to PyPi
	@twine upload dist/*