from wordguess.get_score import get_score

def test_get_score_calculate():
    # Test cases
    assert get_score(["112", "022", "221"], True, 0.1) == 67.5 
    assert get_score(["012", "122"], True, 0.1) == 75.0
    assert get_score(["00000","21222","22222"],True, 0.1) == 81.0
    # assert get_score([], True, 0.1) == 0
    assert get_score(["002", "212", "222"], True, 0.3) == 49.0

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

def test_get_score_valid_strings():
    try:
        get_score(["012", "12A2"])
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for invalid characters in result strings"

    try:
        get_score(["012", "1223"])
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for inconsistent string lengths"
    try:
        get_score(["012", "124"])
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for invalid characters in result strings"

