# This Makefile is not used to compile particular files or sets of
# files, as in a C/C++ project, but instead is used as a task runner
# and centralized point for defining local development tasks.
#
# This Makefile also is an experimental feature for this repository,
# and may be removed without warning.
#
# You can view a list of available tasks by running "make help" or
# just "make".
#
.POSIX:

.PHONY: help
help: ## Display help for this Makefile.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

.DEFAULT: help

# Targets for managing the local development environment.
# ------------------------------------------------------------------------------

.PHONY: clean
clean: ### Clean the local directory of temporary files/artifacts.
	@rm -rf dist/
	@rm -rf .coverage*
	@find . -name '*.egg-info' -exec rm -rf {} +

.PHONY: destroy
destroy: ### Remove the PDM local virtual environment.
	@rm -rf .venv

.PHONY: install
install: ### Set up the local development environment, including pre-commit hooks and local venv.
	@pre-commit install
	@pre-commit install-hooks
	@pdm install

.PHONY: lock
lock: ### Update PDM dependency lockfiles.
	@pdm lock

.PHONY: update
update: ### Update dependencies and tooling.
	@pre-commit autoupdate
	pdm update


# Targets for running tests and checks locally.
# ------------------------------------------------------------------------------

.PHONY: check-docs
check-docs: ### Check the package's documentation.
	@nox -k docs

.PHONY: check-format
check-format: ### Check code formatting.
	@nox -k formatters

.PHONY: check-package
check-package: ### Check the package build and contents.
	@nox -k packaging

.PHONY: ci
ci: ### Run entire CI test/check suite locally: tests with coverage, docs, linters, format checks, package checks.
	@nox -k "not release"

.PHONY: format
format: ### Apply autoformatters to the entire codebase.
	@pre-commit run --all-files black
	@pre-commit run --all-files isort

.PHONY: lint
lint: ### Run linter suite over the codebase.
	@nox -k linters

.PHONY: pre-commit
pre-commit: ### Run all pre-commit hooks.
	@pre-commit run --all-files

.PHONY: test
test: ### Run unit tests with coverage report.
	@nox -k "tests and not release"


# Targets for packaging.
# ------------------------------------------------------------------------------

.PHONY: package
package: ### Build the package.
	@pdm build
