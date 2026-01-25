from wordguess.get_score import get_score
import pytest


def test_get_score_calculate():
    """Testing with sample results and penalties and comparing with expected score"""
    result = ["112", "022", "221"]
    penalty = True
    penalty_rate = 0.1
    expected_score = 67.5
    assert (
        get_score(result=result, penalty=penalty, penalty_rate=penalty_rate)
        == expected_score
    )

    result = ["012", "122"]
    penalty = True
    penalty_rate = 0.1
    expected_score = 75.0
    assert (
        get_score(result=result, penalty=penalty, penalty_rate=penalty_rate)
        == expected_score
    )

    result = ["00000", "21222", "22222"]
    penalty = True
    penalty_rate = 0.1
    expected_score = 81.0
    assert (
        get_score(result=result, penalty=penalty, penalty_rate=penalty_rate)
        == expected_score
    )

    result = ["00000", "21222", "22222"]
    penalty = True
    penalty_rate = 0.3
    expected_score = 49.0
    assert (
        get_score(result=result, penalty=penalty, penalty_rate=penalty_rate)
        == expected_score
    )


def test_get_score_no_penalty():
    """Testing case when no penalty is given"""
    result = ["01122", "02222", "22222"]
    penalty = False
    penalty_rate = 0.0
    expected_score = 100.0
    assert (
        get_score(result=result, penalty=penalty, penalty_rate=penalty_rate)
        == expected_score
    )

    result = ["01122", "22222"]
    penalty = False
    penalty_rate = 0.0
    expected_score = 100.0
    assert (
        get_score(result=result, penalty=penalty, penalty_rate=penalty_rate)
        == expected_score
    )

    result = ["00000", "21222"]
    penalty = False
    penalty_rate = 0.0
    expected_score = 90.0
    assert (
        get_score(result=result, penalty=penalty, penalty_rate=penalty_rate)
        == expected_score
    )

    result = ["111", "122"]
    penalty = True
    penalty_rate = 0.333
    expected_score = 55.58
    assert (
        get_score(result=result, penalty=penalty, penalty_rate=penalty_rate)
        == expected_score
    )


def test_get_score_type_error():
    """
    Testing cases when input type is invalid,
    expecting to throw corresponding errors
    """
    with pytest.raises(TypeError, match="must be a list of strings"):
        get_score("not list")

    with pytest.raises(TypeError, match="must be strings"):
        get_score([123, 456])

    with pytest.raises(TypeError, match="must be strings"):
        get_score(["012", None])

    with pytest.raises(TypeError, match="must be a boolean value"):
        get_score(["012", "122"], penalty="yes")


def test_get_score_value_error():
    """
    Testing when input type is valid but the values do not match the required values,
    expecting to throw corresponding errors
    """
    with pytest.raises(ValueError, match="must only contain characters"):
        get_score(["012", "1242"])

    with pytest.raises(ValueError, match="must have the same length"):
        get_score(["012", "1221"])

    with pytest.raises(ValueError, match="must not be empty"):
        get_score(["012", ""])

    with pytest.raises(ValueError, match="must not be empty"):
        get_score([])

    with pytest.raises(ValueError, match="must be between 0 and 1"):
        get_score(["012", "122"], penalty=True, penalty_rate=1.5)
