# get_score.py
# Author: Harry Yau
# Date: 2026-01-09

def get_score(result: list[str], penalty: bool = False, penalty_rate: float = 0.0) -> float:
    """
    Calculate the score of the guessing.

    This function computes the score based on the provided guess result.
    The calculation will be the highest score from the result list.
    each guess will contain characters '0', '1', and '2' representing different guess outcomes.
    
    Calculation will be sum of of the highest guess score diveded by the total score of the words.
    for example, if the highest guess score is "12222"
    the returning score will be (1+2+2+2+2)/10 * 100 = 90.0

    By default, no penalty is applied. If penalty is set to True, a penalty will be applied for each guess
    before the correct guess. The penalty is calculated as follows:
    For each guess before the correct guess, the score is reduced by the penalty rate of the total score.
    For example, if the correct guess is on the 3rd attempt and the penalty_rate is 0.1, the score will be reduced by 20%.

    Parameters
    ----------
    result : list of str
        A list containing the list of result. The result is a string
        with characters '0', '1', and '2' representing different guess outcomes.

    penalty : bool, optional
        A flag indicating whether to apply a penalty, by default False.
        penalty is applied for each guess before the correct guess.

    penalty_rate : float, optional
        The rate at which the penalty is applied for each incorrect guess, by default 0.0.
        For example, a penalty_rate of 0.1 means a 10% reduction in score for each incorrect guess.

    Returns
    -------
    float
        The calculated score based on the result and penalty flag.

    Examples
    --------
    >>> get_score(["01122", "02222", "22222"])
    100.0
    >>> get_score(["00000", "22222"])
    100.0
    >>> get_score(["01122", "02222", "22222"], penalty=True, 0.1)
    81.0
    >>> get_score(["00000", "21222"])
    90.0

    """
    ...
