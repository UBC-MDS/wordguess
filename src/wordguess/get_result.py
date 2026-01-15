from wordguess._internals import minidict


def get_result(target: str, guess: str, corpus: list = minidict) -> str:
    """
    Generate a guess feedback for a given guess against a target word.

    Parameters
    ----------
    target : str
        The secret word that needs to be guessed.
    guess : str
        The word provided by the player to be compared against the target.
    corpus : list (optional)
        A collection of valid words used for validation.
        Defaults to `minidict`.

    Returns
    -------
    str
        A string of digits representing the result for each letter:
        - '0' : The letter does not exist in the target.
        - '1' : The letter exists in the target but in a different position.
        - '2' : The letter is in the correct position.

    Raises
    ------
    TypeError
        If target or guess are not strings.
    ValueError
        If target and guess have different lengths.
        If the guess is not found in the corpus.

    Examples
    --------
    >>> get_result("apple", "apply")
    '22220'
    >>> get_result("stare", "tears")
    '11211'
    >>> get_result("books", "slope")
    '00201'
    """
    
    ## Invalid input checks
    if not isinstance(target, str) or not isinstance(guess, str):
        # either target or guess is not a string
        raise TypeError("Target and guess must be strings")
    if len(target) != len(guess):
        # target and guess lengths do not match
        raise ValueError("Target and guess must be of the same length")
    if target not in corpus:
        # target is not in the valid word list
        raise ValueError(f"'{target}' is not a valid word")
    if guess not in corpus:
        # guess is not in the valid word list
        raise ValueError(f"'{guess}' is not a valid word")

    # Initialize target and guess lists
    target_pool = list(target)
    guess_list = list(guess)

    # 0 (default); initialize result list
    result = ["0"] * len(guess)

    # 2
    for i in range(len(guess)):
        if guess_list[i] == target_pool[i]:
            result[i] = "2"
            target_pool[i] = None
            guess_list[i] = None

    # 1
    for i in range(len(guess)):
        current_letter = guess_list[i]
        if current_letter is None:
            continue
        if current_letter in target_pool:
            result[i] = "1"
            target_pool.remove(current_letter)

    return "".join(result)
