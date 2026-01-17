from ._internals import minidict
import random
from collections import defaultdict

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
    
    # keeping a letter-by-letter map
    mem = defaultdict(list)

    # keeping a word map
    final_ones = []
    final_twos = [None for _ in range(len(guess))]

    for guess, result in result_hist.items():
        guess = guess.lower()
        result = result.lower()
        for pos in range(len(guess)):
            letter = guess[pos]
            res = result[pos]
            # handling duplicate letter. Eg. speed will be coded with e and e1
            if guess[:pos].count(letter): 
                letter=letter+str(guess[:pos].count(letter))

            if res == '1': final_ones.append(letter)
            if res == '2':
                # check for positional conflict
                if final_twos[pos] and final_twos[pos]!=letter:
                    raise ValueError(f"Positional Conflict between {letter} and {final_twos[pos]} at position {pos}")
                else:
                    final_twos[pos]=letter

            # add to mem for this letter
            mem[letter].append((pos, res))

    # check if over constrained (too many letters)
    if len(set(final_ones+final_twos)) > len(guess):
        raise ValueError(f"Too many letters present in target")
    
    # loop through all letters and check for inconsistency
    for letter, data in mem.items():
        zeros = [x[0] for x in data if x[1] == '0']
        ones = [x[0] for x in data if x[1] == '1']
        twos =  [x[0] for x in data if x[1] == '2']
        if zeros and ones or zeros and twos:
            raise ValueError(f"Presence ambiguity in letter {letter[:1]}")
        if bool(set(ones) & set(twos)):
            raise ValueError(f"Positional ambiguity in letter {letter[:1]}")
    
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
            word_lower = word.lower()
            
            # Count letter requirements
            min_letter_counts = defaultdict(int)
            max_letter_counts = defaultdict(lambda: float('inf'))
            
            for pos in range(len(guess)):
                letter = guess[pos]
                res = result[pos]
                
                if res in ['1', '2']:
                    min_letter_counts[letter] += 1
                elif res == '0':
                    # '0' means this specific occurrence is excess
                    # Set max to the count of '1's and '2's for this letter
                    max_letter_counts[letter] = min_letter_counts[letter]
            
            # Check positional constraints
            for pos in range(len(guess)):
                letter = guess[pos]
                res = result[pos]
                
                if res == '1':
                    if letter not in word_lower or word_lower[pos] == letter:
                        valid = False
                        break
                elif res == '2':
                    if word_lower[pos] != letter:
                        valid = False
                        break
            
            # Check count constraints
            if valid:
                for letter in set(guess):
                    count = word_lower.count(letter)
                    if count < min_letter_counts[letter] or count > max_letter_counts[letter]:
                        valid = False
                        break
            
            if not valid:
                break

        if valid:
            possible_guesses.append(word)
    
    for guess in result_hist:
        while guess in possible_guesses:
            possible_guesses.remove(guess)
    
    if n and n < len(possible_guesses): 
        return random.sample(possible_guesses, n)
    return possible_guesses
