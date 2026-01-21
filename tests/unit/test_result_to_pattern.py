"""
A test module that tests the result_to_pattern module.
"""

import pytest
from wordguess.result_to_pattern import result_to_pattern


def test_result_to_pattern():
    """
    Test that result_to_pattern works as expected.
    """
    result_1 = "01210"
    expected_1 = "⬛🟨🟩🟨⬛"
    actual_1 = result_to_pattern(result_1)
    assert actual_1 == expected_1, f"Expected {expected_1} but got {actual_1}"

    result_2 = "000"
    expected_2 = "⬛⬛⬛"
    actual_2 = result_to_pattern(result_2)
    assert actual_2 == expected_2, f"Expected {expected_2} but got {actual_2}"

    result_3 = ""
    expected_3 = ""
    actual_3 = result_to_pattern(result_3)
    assert actual_3 == expected_3, f"Expected {expected_3} but got {actual_3}"


def test_result_to_pattern_input_type():
    """
    Test that result_to_pattern throws an error when the
    input is the incorrect type (i.e., not a string).
    """
    result_1 = 12100
    with pytest.raises(TypeError):
        result_to_pattern(result_1)

    result_2 = ["0", "1", "2", "0"]
    with pytest.raises(TypeError):
        result_to_pattern(result_2)

    result_3 = ["01002", "10202"]
    with pytest.raises(TypeError):
        result_to_pattern(result_3)


def test_result_to_pattern_chars():
    """
    Test that result_to_pattern throws an error when the
    input contains characters other than '0', '1' or '2'.
    """
    result_1 = "12300"
    with pytest.raises(ValueError):
        result_to_pattern(result_1)

    result_2 = "89671"
    with pytest.raises(ValueError):
        result_to_pattern(result_2)

    result_3 = "wordle"
    with pytest.raises(ValueError):
        result_to_pattern(result_3)
