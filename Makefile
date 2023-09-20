#################################################################################
# GLOBALS                                                                       #
#################################################################################

-include .envrc
export

PYTHON_INTERPRETER = python3

#################################################################################
# COMMANDS                                                                      #
#################################################################################

.PHONY: help
help:	## Show this help.
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: pre-commit
pre-commit: ## Runs the pre-commit over entire repo
	@poetry run pre-commit run --all-files

define install_dependencies
	if ! type "poetry" > /dev/null; then \
		pip install poetry; \
	fi
	poetry config virtualenvs.in-project true
	poetry install --sync --with dev
endef

.PHONY: install
install: ## Install dependencies
	@$(call install_dependencies)

.PHONY: clean
clean: ## Delete all Python cache files
	@find . -type d -name "__pycache__" -prune -exec rm -rf {} \; &&\
	find . -type d -name ".pytest_cache" -prune -exec rm -rf {} \; &&\

.PHONY: test
test: ## Run all unit tests locally
	@poetry run python -m pytest -s .

.PHONY: dev
dev: ## Run API locally
	@poetry run python -m uvicorn canary.src.main:app --reload --port=8000
