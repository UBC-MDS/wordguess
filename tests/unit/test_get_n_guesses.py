import pytest
from wordguess.get_n_guesses import get_n_guesses
from wordguess._internals import minidict

# ---------- Input validation ----------

def test_invalid_result_histories():
    # ---------- Invalid input structure ----------
    with pytest.raises(TypeError):
        get_n_guesses(['hello','10001'])

    with pytest.raises(TypeError):
        get_n_guesses({'hello': 10010})

    with pytest.raises(ValueError):
        get_n_guesses({'hello': '100001'})

    with pytest.raises(ValueError):
        get_n_guesses({'zxcnw': '00100'})

    with pytest.raises(ValueError):
        get_n_guesses({'hello': '12300'})


# ---------- Consistency conflicts ----------

def test_result_history_conflicts():
    # ---------- Conflict 2 to 1 ----------
    with pytest.raises(ValueError):
        get_n_guesses({
        "under": "00200",
        "index": "00100"
    })
        
    # ---------- Conflict 1 to 2-----------
    with pytest.raises(ValueError):
        get_n_guesses({
        "about": "10000",
        "angle": "20000"
    })

    # ---------- Conflict 2 to 0 ----------
    with pytest.raises(ValueError):
        get_n_guesses({
        "about": "20000",
        "angle": "02000"
        }
    )
        
    # ---------- Conflict 0 to 2 -----------
    with pytest.raises(ValueError):
        get_n_guesses({
        "about": "00000",
        "angle": "20000"
    })
        
    # ---------- Conflict 1 to 0 -----------
    with pytest.raises(ValueError):
        get_n_guesses({
        "about": "10000",
        "angle": "00000"
    })
        
    # ---------- Conflict 0 to 1 -----------
    with pytest.raises(ValueError):
        get_n_guesses({
        "about": "00000",
        "angle": "10000"
    })
        
    # ------ too many letters present ----------
    with pytest.raises(ValueError):
        get_n_guesses({
        "about": "11111",
        "angle": "11000"
    })

# ---------- Basic filtering behavior ----------

def test_empty_history_returns_all():
    result = get_n_guesses({}, corpus=minidict)
    assert set(result) == set(minidict)


def test_single_zero_constraint():
    result = get_n_guesses({"crane": "00000"}, corpus=minidict)
    for word in result:
        assert 'c' not in word
        assert 'r' not in word
        assert 'a' not in word
        assert 'n' not in word
        assert 'e' not in word


def test_correct_position_constraint():
    result = get_n_guesses({"crane": "20000"}, corpus=minidict)
    for word in result:
        assert word[0] == 'c', f"Word {word} doesn't have 'c' at position 0"


def test_wrong_position_constraint():
    result = get_n_guesses({"crane": "10000"}, corpus=minidict)
    for word in result:
        assert 'c' in word, f"Word {word} doesn't contain 'c'"
        assert word[0] != 'c', f"Word {word} has 'c' at position 0"


# ---------- Multiple constraints ----------

def test_multiple_guess_constraints():
    result_hist = {
        "crane": "01200",
        "sloth": "10020"
    }

    result = get_n_guesses(result_hist, corpus=minidict)

    for word in result:
        # From crane: c, n, e not in word; r in word but not pos 1; a at pos 2
        assert 'c' not in word
        assert 'n' not in word
        assert 'e' not in word
        assert word[2] == 'a'
        if 'r' in word:
            assert word[1] != 'r'
        # From sloth: l, o, h not in word; s in word but not pos 0; t at pos 3
        assert 'l' not in word
        assert 'o' not in word
        assert 'h' not in word
        assert word[3] == 't'
        if 's' in word:
            assert word[0] != 's'


# ---------- n parameter behavior ----------

def test_n_parameter():
    assert len(get_n_guesses({}, n=10, corpus=minidict)) == 10

    # only one possible target, but removed from guesses
    assert get_n_guesses({"crane": "22222"}, n=100, corpus=minidict) == []

    result_all = get_n_guesses({"apple": "00000"}, corpus=minidict)
    result_n_none = get_n_guesses({"apple": "00000"}, n=None, corpus=minidict)
    assert set(result_all) == set(result_n_none)

    assert len(get_n_guesses({}, n=1, corpus=minidict)) == 1


# ---------- Duplicate-letter logic ----------

def test_repeated_letter_handling():
    corpus_test = ["speak", "speed", "spear"]
    result_hist = {"speed": "22210"}  # target = speak

    result = get_n_guesses(result_hist, corpus=corpus_test)
    assert "speed" not in result
    assert "speak" in result
