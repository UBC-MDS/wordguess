"""
A module that calculate the score of the guessing word.
this function will take a list of integer list as input and return a score

"""
def get_score(guesses: list[list[int]], penalty: bool = False) -> float:
    """
    Calculate the score of the guessing.

    This function computes the score based on the provided guesses.

    Parameters
    ----------
    guesses : list of list of int
        A list containing lists of integers representing guesses.

    penalty : bool, optional
        A flag indicating whether to apply a penalty, by default False.

    Returns
    -------
    float
        The calculated score based on the guesses and penalty flag.

    Examples
    --------
    >>> get_score([[0, 1, 1, 2, 2], [0, 2, 2, 2, 2], [2, 2, 2, 2, 2]])
    100.0
    >>> get_score([[0, 0, 0, 0, 0], [2, 2, 2, 2, 2]])
    100.0
    >>> get_score([[0, 1, 1, 2, 2], [0, 2, 2, 2, 2], [2, 2, 2, 2, 2]], penalty=True)
    81.0
    >>> get_score([[0, 0, 0, 0, 0], [2, 1, 2, 2, 2]])
    0.0

    """
    ...