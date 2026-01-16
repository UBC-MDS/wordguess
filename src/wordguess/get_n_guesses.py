from ._internals import minidict
import random

def check_dict_validity(result_hist, corpus=minidict):
    guess = ""
    for guess, result in result_hist.items():
        if not isinstance(guess, str) or not isinstance(result, str):
            raise TypeError(f"Passed key-value pair {guess}-{result} is not of type `string`")
        if len(guess) != len(result):
            raise ValueError(f"result '{result}' length does not match input length for '{guess}'")
        if len(guess) == 0:
            raise ValueError(f"Zero length strings passed")
        if guess not in corpus:
            raise ValueError(f"The guess '{guess}' is not present in the corpus")

    zeros = []
    ones = dict()
    final_target = [None for _ in range(len(guess))]
    
    str_len = len(guess)

    for guess, result in result_hist.items():
        guess = guess.lower()
        result = result.lower()
        for pos in range(len(guess)):
            letter = guess[pos]
            res = result[pos]
            if res == '0':
                if letter in ones or letter in final_target:
                    raise ValueError(f"Character {letter} has inconsistent history, presence ambiguity in {guess}")
                if letter not in zeros:
                    zeros.append(letter)
            if res == '1':
                if letter in zeros:
                    raise ValueError(f"Character {letter} has inconsistent history, presence ambiguity in {guess}")
                if letter in final_target and pos == final_target.index(letter):
                    raise ValueError(f"Character {letter} has inconsistent history, positional ambiguity in {guess}")
                if letter not in ones:
                    ones[letter]=pos
            if res == '2':
                if final_target[pos] and final_target[pos] != letter:
                    raise ValueError(f"Character {letter} conflicts with character {final_target[pos]} for position {pos}")
                if letter in zeros:
                    raise ValueError(f"Character {letter} has inconsistent history, presence ambiguity in {guess}")
                if letter in ones and ones[letter]==pos:
                    raise ValueError(f"Character {letter} has inconsistent history, positional ambiguity in {guess}")
                final_target[pos] = letter
    if len(set(list(ones.keys())+final_target)) > str_len:
        raise ValueError(f"Too many letters present in target")
    return True

def get_n_guesses(result_hist: dict, n: int = None, corpus: list = minidict) -> list:
    """
    Return all possible target words consistent with the result history.

    This function filters the given corpus of allowed words using the information
    contained in a result history. Each entry in the result history consists of
    a guessed word and its corresponding result string, where:
    - '0' indicates the letter is not present in the target word,
    - '1' indicates the letter is present but in the wrong position, and
    - '2' indicates the letter is correct and in the correct position.

    Words in the corpus that violate any of the constraints implied by the result
    history are eliminated and the remaining words are considered to be possible
    valid guesses. If the parameter n is provided, n random words from the valid
    guesses are returned. If n is None, all valid guesses are returned.

    Parameters
    ----------
    result_hist : dict
        A dictionary mapping previously guessed words to their
        corresponding result strings composed of '0', '1', and '2'.
    n : int (optional)
        The number of valid guesses to return.
        If None, all valid guesses are returned.
    corpus : list (optional)
        A list of all allowed words to consider as possible targets.

    Returns
    -------
    list: A list of words from the corpus that are consistent with the result history.

    See Also
    --------
    get_result : A function that generate the result string for a given guess against a target word.

    Examples
    --------
    >>> result_hist = {"crane": "01200", "sloth": "10020"}
    >>> get_n_guesses(result_hist, corpus=corpus)
    ['about', 'shout', 'mount']

    >>> get_n_guesses(result_hist, n=2, corpus=corpus)
    ['shout', 'mount']
    """
    # input types
    if not isinstance(result_hist, dict):
        raise TypeError(f"Passed `result_hist` was not a valid dictionary")
    if n and (not isinstance(n, int) or n<0):
        raise TypeError(f"Passed `n` was not a positive integer")
    if not isinstance(corpus, list):
        raise TypeError(f"Passed `corpus` was not a valid list of strings")
    # check if result dict is valid
    if not check_dict_validity(result_hist, corpus):
        raise ValueError(f"Passed `result_hist` is not consistent")
        
    possible_guesses = []
    for word in corpus:
        valid = True
        for guess, result in result_hist.items():
            guess = guess.lower()
            result = result.lower()
            for pos in range(len(guess)):
                letter = guess[pos]
                res = result[pos]

                if res == '0' and letter in word:
                    valid = False
                    break
                elif res == '1':
                    if letter not in word or letter == word[pos]:
                        valid = False
                        break
                elif res == '2' and letter != word[pos]:
                    valid = False
                    break
            if not valid:
                break

        if valid:
            possible_guesses.append(word)
    for guess in result_hist:
        while guess in possible_guesses:
            possible_guesses.remove(guess)
    if n and n<len(possible_guesses): 
        return random.sample(possible_guesses, n)
    return possible_guesses
