from ._internals import minidict


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
    # TODO: write checks for input
    # TODO: write the function body
    return corpus
