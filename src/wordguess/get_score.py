# get_score.py
# Author: Harry Yau
# Date: 2026-01-09


def get_score(
    result: list[str], penalty: bool = False, penalty_rate: float = 0.0
) -> float:
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

    Raises
    ------
    TypeError
        If result is not a list of strings or penalty is not a boolean.
    ValueError
        If result strings contain invalid characters.
        If result strings do not have the same length.
        If any result string is empty.

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
    if not isinstance(result, list):
        raise TypeError("Result must be a list of strings.")
    if not all(isinstance(r, str) for r in result):
        raise TypeError("All elements in result must be strings.")
    if not isinstance(penalty, bool):
        raise TypeError("Penalty must be a boolean value.")
    if result == []:
        raise ValueError("Result list must not be empty.")
    if penalty_rate < 0 or penalty_rate > 1:
        raise ValueError("Penalty rate must be between 0 and 1.")
    if any(r == "" for r in result):
        raise ValueError("All result strings must not be empty.")
    if not all(all(c in "012" for c in r) for r in result):
        raise ValueError(
            "Result strings must only contain characters '0', '1', and '2'."
        )
    if len(set(len(r) for r in result)) > 1:
        raise ValueError("All result strings must have the same length.")

    total_score = len(result[0]) * 2
    highest_score = 0

    for res in result:
        current_score = sum(int(c) for c in res)
        if current_score == total_score:
            highest_score = current_score
            break
        if current_score > highest_score:
            highest_score = current_score

    score_percentage = (highest_score / total_score) * 100

    if penalty:
        penalty_multiplier = (1 - penalty_rate) ** (len(result) - 1)
        score_percentage *= penalty_multiplier

    return round(score_percentage, 2)
