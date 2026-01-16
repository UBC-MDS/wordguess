from wordguess.get_score import get_score
import pytest

def test_get_score_calculate():
    result = ["112", "022", "221"]
    penalty = True
    penalty_rate = 0.1
    expected_score = 67.5
    assert get_score(result=result, penalty=penalty, penalty_rate=penalty_rate) == expected_score 

    result = ["012", "122"]
    penalty = True
    penalty_rate = 0.1
    expected_score = 75.0
    assert get_score(result=result, penalty=penalty, penalty_rate=penalty_rate) == expected_score 

    result = ["00000","21222","22222"]
    penalty = True
    penalty_rate = 0.1
    expected_score = 81.0
    assert get_score(result=result, penalty=penalty, penalty_rate=penalty_rate) == expected_score 

    result = ["00000","21222","22222"]
    penalty = True
    penalty_rate = 0.3
    expected_score = 49.0
    assert get_score(result=result, penalty=penalty, penalty_rate=penalty_rate) == expected_score 

def test_get_score_no_penalty():
    result = ["01122", "02222", "22222"]
    penalty = False
    penalty_rate = 0.0
    expected_score = 100.0
    assert get_score(result=result, penalty=penalty, penalty_rate=penalty_rate) == expected_score 

    result = ["01122", "22222"]
    penalty = False
    penalty_rate = 0.0
    expected_score = 100.0
    assert get_score(result=result, penalty=penalty, penalty_rate=penalty_rate) == expected_score 

    result = ["00000", "21222"]
    penalty = False
    penalty_rate = 0.0
    expected_score = 90.0
    assert get_score(result=result, penalty=penalty, penalty_rate=penalty_rate) == expected_score 

def test_get_score_types():
    with pytest.raises(TypeError):
        get_score("not list")
        assert False, "Expected TypeError for non-list input"

    with pytest.raises(TypeError):
        get_score([123, 456])
        assert False, "Expected TypeError for non-string elements in list"
    with pytest.raises(TypeError):
        get_score(["012", "122"], penalty="yes")
        assert False, "Expected TypeError for non-boolean penalty"

def test_get_score_valid_strings():
    with pytest.raises(ValueError):
        get_score(["012", "12A2"])
        assert False, "Expected ValueError for invalid characters in result strings"
    with pytest.raises(ValueError):
        get_score(["012", "1223"])
        assert False, "Expected ValueError for inconsistent lengths of result strings"
    with pytest.raises(ValueError):
        get_score(["012", "124"])
        assert False, "Expected ValueError for invalid characters in result strings"

