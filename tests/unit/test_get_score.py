from src.wordguess.get_score import get_score

def test_get_score_calculate():
    # Test cases
    assert get_score(["112", "022", "221"], True, 0.1) == 5/6*100 * 0.9 * 0.9
    assert get_score(["012", "122"], True, 0.1) == 5/6*100 * 0.9
    assert get_score(["00000","21222","22222"],True, 0.1) == 100 * 0.9 * 0.9
    assert get_score([], True, 0.1) == 0
    assert get_score([0, 0, 2], [2, 1, 2], [2, 2, 2], True, 0.3) == 100 * 0.7 * 0.7

def test_get_score_no_penalty():
    assert get_score(["01122", "02222", "22222"]) == 100.0
    assert get_score(["00000", "22222"]) == 100.0
    assert get_score(["00000", "21222"]) == 90.0

def test_get_score_types():
    try:
        get_score("not list")
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError for non-list input"

    try:
        get_score([123, 456])
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError for non-string elements in list"
    try:
        get_score(["012", "122"], penalty="yes")
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError for non-boolean penalty"
