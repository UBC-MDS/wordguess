from _internals import minidict


def get_result(target: str, guess: str, corpus: list = minidict) -> str:
    """
    Generate a guess feedback for a given guess against a target word.

    Parameters
    ----------
    target : str
        The secret word that needs to be guessed.
    guess : str
        The word provided by the player to be compared against the target.
    corpus : list, optional
        A collection of valid words used for validation.
        Defaults to `minidict`.

    Returns
    -------
    str
        A string of digits representing the result for each letter:
        - '0' : The letter does not exist in the target.
        - '1' : The letter exists in the target but in a different position.
        - '2' : The letter is in the correct position.

    Examples
    --------
    >>> get_result("apple", "apply")
    '22220'
    >>> get_result("stare", "tears")
    '11211'
    >>> get_result("books", "slope")
    '00201'
    """

    pass
