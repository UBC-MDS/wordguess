# Changelog

All notable changes to this project will be documented in this file.

## [0.0.1] - 2026-01-10

- Initial setup of the project
- Added project summary
- Added code of conduct
- Added contribution guidelines
- Added installation instructions
- Added usage examples
- Added definitions of key terms
- Added `minidict` dataset
- Added function specifications for `get_result`
- Added function specifications for `get_n_guesses`
- Added function specifications for `get_score`
- Added function specifications for `result_to_pattern`

## [1.0.0] - 2026-01-17

- Updated `minidict` dataset with additional words
- Updated usage examples for additional complex scenarios
- Updated installation instructions from GitHub repository
- Updated function specifications for `get_score`
- Added function implementation for `get_result`
- Added function implementation for `get_n_guesses`
- Added function implementation for `get_score`
- Added function implementation for `result_to_pattern`
- Added tests for `get_result`
- Added tests for `get_n_guesses`
- Added tests for `get_score`
- Added tests for `result_to_pattern`
- Added package-level imports in `__init__.py`

## [2.0.0] - 2026-01-24

- Fixed typos and format issues
- Fixed code linting errors
- Updated `README.md` with installation and development guides
- Updated `CONTRIBUTING.md` with code formatter and linter change
- Updated `CONTRIBUTING.md` with hyperlinks
- Updated `CODE_OF_CONDUCT.md` with enforcement guidelines and contact info
- Added documentation site
- Added Quarto configuration for documentation site
- Added Quarto-related dependencies
- Added `environment.yml` for development environment setup
- Added `index.qmd` as documentation homepage
- Added GitHub Actions workflow for package building and testing
- Added GitHub Actions workflow for code quality checks
- Added GitHub Actions workflow for publishing package to TestPyPI
- Added GitHub Actions workflow for documentation rendering and publishing
- Added one more test case in `tests/unit/test_result_to_pattern.py`
- Added three test cases in `tests/unit/test_get_score.py`
- Added one more test case in `tests/unit/test_get_result.py`
- Added validation for penalty rate in `src/wordguess/get_score.py`
- Added validation for empty result lists in `src/wordguess/get_score.py`
- Removed unused `docs` directory and Sphinx configuration
- Removed unused GitHub Actions workflows
- Removed Sphinx-related dependencies from `pyproject.toml`

## [3.0.0] - 2026-02-02

- Fixed errors when running examples in `README.md` and docstrings (with many thanks to the peer review)
- Added step-by-step tutorials to `README.md` and documentation site (with many thanks to the peer review)
- Added `CHANGELOG.md` to the documentation site
- Added badges to `README.md` for PyPI version, build status, code quality, and documentation status
- Added more words to `minidict` dataset
- Added more in-line comments to user functions (with many thanks to the peer review)
- Added work organization and retrospectives to `CONTRIBUTING.md`
- Added GitHub Actions workflow for dynamic versioning
- Added GitHub Actions workflow for previewing documentation site
- Added GitHub Actions workflow for code coverage reporting
- Removed redundant signs in the example code snippets in `README.md` (with many thanks to the peer review)
