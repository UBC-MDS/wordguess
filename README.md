# Welcome to wordguess

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/wordguess.svg)](https://pypi.org/project/wordguess/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/wordguess.svg)](https://pypi.org/project/wordguess/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

Wordguess is a project that contains essential functions for a word-guessing game, inspired by [Wordle](https://www.nytimes.com/games/wordle/index.html).

## Summary

The `wordguess` package is designed for developers to create guessing games. The package provides functionality for word validation, feedback generation, and corpus management. It can compare user guesses to the target word and provide feedback on the accuracy of the guesses in terms of correct letters and their positions, including numerical and human-readable expressions. Additionally, features for scoring and hinting are included to enhance development of word-guessing games. `wordguess` provides the back-end foundation needed to handle the underlying string comparisons and state tracking.

`wordguess` fits perfectly into the Python ecosystem by offering a simple foundation for word-based projects. It uses standard Python practices, making it a great tool for learning to code or for developers who want to quickly add logic to their game ideas. Because the package emphasizes clean type-hinting and standardized docstrings, it serves as an excellent resource for developers learning about string manipulation, algorithmic logic, and package distribution. It bridges the gap between simple script-based games and production-ready modular code.

## Collaborators

* Sarisha Das
* Sarah Gauthier
* Yuheng Ouyang
* Harry Yau

## Get started

You can install this package into your preferred Python environment using pip:

```bash
pip install -i https://test.pypi.org/simple/ wordguess
``````

To use `wordguess` in your code:

```python
>>> from wordguess.get_result import get_result
>>> get_result("spark", "spoon")
```

```python
>>> import wordguess as wg
>>> 
>>> result_hist = {}
>>> for word in ['whelp','might','madam']:
>>>     result_hist[word] = wg.get_result('major', word)
>>>     wg.get_n_guesses(result_hist, n=10)
```

## Development

To contribute to this project, please refer to the [contribution guidelines](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md).

### Setting up a development environment

You can set up a development environment by cloning the repository and installing the dependencies (we recommend using `conda`):

```bash
conda env create -f environment.yml
```

Creating a conda environment includes installing the package in editable mode for development. If you are not using `conda`, you can install it manually:

```bash
pip install -e .[dev]  # not required if using the above conda setup
```

### Running tests

To run the test suite, use:

```bash
pytest
```

### Building documentation

Documentation needs to be updated when changes are made. You can build the documentation locally using `quartodoc`:

```bash
quartodoc build
```

After reviewing and fixing the auto-generated `.qmd` files, you can preview the documentation to HTML:

```bash
quarto preview
```

### Code style

We follow the [PEP 8](https://peps.python.org/pep-0008/) style guide for Python code. [Ruff](https://docs.astral.sh/ruff/linter/) is integrated in the development environment to help maintain code quality.

### Repository structure

The project repository contains three protected branches. All new features and bug fixes should be developed in independent development branches created from `otter`. Once changes are complete and tested, a pull request should be opened to merge the development branch back into `otter`. After review, changes from `otter` can be merged into `main` for release.

* `main`: the production branch containing the latest stable release. When merged from `otter`,
  * code style is checked  (pass enforced);
  * test suites are run (pass enforced);
  * documentation is built and published;
  * a new release is created; and
  * the new release published to TestPyPI from the `main` branch.
* `otter`: the staging branch where new features and bug fixes are integrated before release. When merged from a development branch,
  * code style is checked (pass enforced); and
  * test suites are run (pass enforced).
* `gh-pages`: the branch containing the published documentation website. This should only be updated via automated workflows.

## Dataset & user functions

Full API reference can be viewed at [https://ubc-mds.github.io/wordguess/reference/](https://ubc-mds.github.io/wordguess/reference/).

* Dataset: `minidict` (*list*)
  * **Location:** `/src/wordguess/_internals.py`
  * **Description:** A default list of more than 600 valid and non-valid English words, each five letters in length. This serves as the fallback `corpus` for all functions unless a custom list is provided. This example dataset is generated by [Claude Sonnet 4.5](https://www.anthropic.com/news/claude-sonnet-4-5).

* `get_result(target, guess, corpus=minidict)`
  * **Location:** `/src/wordguess/get_result.py`
  * **Description:** Compares a `guess` against a `target` and returns the comparison `result`.
  * **Parameters:**
    * **target** (*str*): The secret word to be guessed.
    * **guess** (*str*): The player's attempt.
    * **corpus** (*list*, optional): A list of valid words for validation. Defaults to `minidict`.
  * **Returns:** (*str*) A string of digits ('0', '1', '2') mapping the relationship between letters.

* `get_score(result, penalty=False, penalty_rate=0.0)`
  * **Location:** `/src/wordguess/get_score.py`
  * **Description:** Calculates a numerical `score` representing the "goodness" of a series of `result`s.
  * **Parameters:**
    * **result** (*list of str*): A list of `result` strings from previous guesses.
    * **penalty** (*bool*, optional): Whether to apply a penalty for incorrect guesses. Defaults to `False`.
    * **penalty_rate** (*float*, optional): The rate at which penalties are applied. Defaults to `0.0`.
  * **Returns:** (*float*) A score between 0 and 100.

* `get_n_guesses(result_hist, n, corpus)`
  * **Location:** `/src/wordguess/get_n_guesses.py`
  * **Description:** Returns all possible target words consistent with the result history.
  * **Parameters:**
    * **result_hist** (*dict*): A dictionary mapping previously guessed words to their corresponding results.
    * **n** (*int*, optional): The maximum number of relative words to return.
    * **corpus** (*list*, optional): The library of words to search. Defaults to `minidict`.
  * **Returns:** (*list*) A list of the top `n` strings.

* `result_to_pattern(result)`
  * **Location:** `/src/wordguess/result_to_pattern.py`
  * **Description:** Converts a numerical `result` string into a human-readable `pattern` using [UTF-8 Colored Symbols](https://www.utf8icons.com/).
  * **Parameters:**
    * **result** (*str*): A string of 0s, 1s, and 2s.
  * **Returns:** (*str*) A visual string of emojis (e.g., 🟩, 🟨, ⬛).

## Key definitions

To ensure consistency for **users** (developers) and **players** (end-users), the following terminology is used throughout the package:

| Term | Definition |
| --- | --- |
| **User** | The developer interacting with this package. |
| **Player** | The person playing the word-guessing game. |
| **Target** | The specific word chosen to be guessed. |
| **Guess** | The string submitted by the player to match the target. |
| **Corpus / Dataset** | A list of words (like `minidict`) used as the search space. |
| **Result** | A string of 0, 1, 2 indicating letter status (0=None, 1=Wrong Spot, 2=Correct). |
| **Pattern** | The visual, emoji-based representation of a **Result**. |
| **Score** | A numerical value quantifying how close a **Guess** is to a **Target**. |

## LLM usage disclosure

Large language models (LLMs) are involved in assisting test development, code review, and corpus generation.

| Model | Usage | Last Accessed |
| --- | --- | --- |
| [Claude Sonnet 4.5](https://www.anthropic.com/news/claude-sonnet-4-5) | Corpus generation, script review and optimization | January 2026 |
| [GitHub Copilot](https://github.com/features/copilot) | Pull request review, code fix, style consistency | January 2026 |
| [GPT-5.2](https://openai.com/index/introducing-gpt-5-2/) | Test coverage review and improvement | January 2026 |

## Copyright

* Copyright © 2026 Sarisha Das, Sarah Gauthier, Yuheng Ouyang, Harry Yau.
* Free software distributed under the [MIT License](./LICENSE).
