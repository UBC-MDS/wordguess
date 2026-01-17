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
$ pip install git+https://github.com/UBC-MDS/wordguess.git
```

To use `wordguess` in your code:

```python
>>> from wordguess.get_result import get_result
>>> get_result("spark", "spoon")
```

```python
>>> from wordguess.get_n_guesses import get_n_guesses
>>> from wordguess.get_result import get_result
>>> 
>>> result_hist = {}
>>> for word in ['whelp','might','madam']:
>>>   result_hist[word] = get_result('major',word)
>>>   get_n_guesses(result_hist, n=10)
```

## Dataset & user functions

* Dataset: `minidict` (*list*)
  * **Location:** `/src/wordguess/_internals.py`
  * **Description:** A default list of more than 600 valid and non-valid English words, each five letters in length. This serves as the fallback `corpus` for all functions unless a custom list is provided.

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
    * **result** (*list[str]*): A list of `result` strings from previous guesses.
    * **penalty** (*bool*, optional): Whether to apply a penalty for incorrect guesses. Defaults to `False`.
    * **penalty_rate** (*float*, optional): The rate at which penalties are applied. Defaults to `0.0`.
  * **Returns:** (*float*) A score between 0 and 100.

* `get_n_guesses(result_hist, n, corpus)`
  * **Location:** `/src/wordguess/get_n_guesses.py`
  * **Description:** Returns all possible target words consistent with the result history.
  * **Parameters:**
    * **result_hist** (*dict*): A dictionary mapping previously guessed words to their corresponding results.
    * **n** (*int*, optional): The number of relative words to return.
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
| **Corpus / Dataset** | A list of English words (like `minidict`) used as the search space. |
| **Result** | A string of 0, 1, 2 indicating letter status (0=None, 1=Wrong Spot, 2=Correct). |
| **Pattern** | The visual, emoji-based representation of a **Result**. |
| **Score** | A numerical value quantifying how close a **Guess** is to a **Target**. |

## Copyright

- Copyright © 2026 Sarisha Das, Sarah Gauthier, Yuheng Ouyang, Harry Yau.
- Free software distributed under the [MIT License](./LICENSE).
