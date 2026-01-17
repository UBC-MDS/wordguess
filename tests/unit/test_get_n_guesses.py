import pytest
from wordguess.get_n_guesses import get_n_guesses
from wordguess._internals import minidict

def test_invalid_result_histories():
    # ---------- Invalid input structure ----------
    with pytest.raises(TypeError):
        get_n_guesses(['hello','10001'])

    with pytest.raises(TypeError):
        get_n_guesses({'hello': 10010})

    with pytest.raises(ValueError):
        get_n_guesses({'hello': '100001'})

    # not present in corpus
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
        
    # ------ two letters on same position ----------
    with pytest.raises(ValueError):
        get_n_guesses({
        "about": "02000",
        "angle": "02000"
    })
        
    # ------ too many letters present ----------
    # only 1s
    with pytest.raises(ValueError):
        get_n_guesses({
        "about": "11111",
        "angle": "11000"
    })
    # 1s and 2s
    with pytest.raises(ValueError):
        get_n_guesses({
        "about": "11211",
        "angle": "11000"
    })

# ---------- Basic filtering behavior ----------

def test_empty_history_returns_all():
    # returns whole corpus for empty history
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

def test_correct_word_guesses():
    result = get_n_guesses({"crane": "22222"}, corpus=minidict)
    assert result == []

def test_target_outside_corpus():
    with pytest.raises(ValueError):
        get_n_guesses({"crane": "22211"}, corpus=minidict)
        
# ---------- Multiple constraints ----------

def test_multiple_guess_constraints():
    result_hist = {
        "repay": "10000",
        "print": "01001",
        "motor": "02101"
    }
    

    result = get_n_guesses(result_hist, corpus=minidict)

    for word in result:
        assert 'r' in word
        assert word[0] != 'r'
        assert 'e' not in word
        assert 'p' not in word
        assert 'a' not in word
        assert 'y' not in word
        
        assert word[1] != 'r'
        assert 'i' not in word
        assert 'n' not in word
        assert 't' in word
        assert word[4] != 't'
        
        assert 'm' not in word
        assert word[1] == 'o'
        assert word[2] != 't'
        assert word[3] != 'o'
        
        assert word.count('o') == 1
        
    assert "repay" not in result
    assert "print" not in result
    assert "motor" not in result


# ---------- n parameter behavior ----------

def test_n_parameter():
    assert len(get_n_guesses({}, n=10, corpus=minidict)) == 10
    assert len(get_n_guesses({}, n=1, corpus=minidict)) == 1

    with pytest.raises(TypeError):
        get_n_guesses({}, n=1.0)
    with pytest.raises(TypeError):
        get_n_guesses({}, n=-1)

# ---------- Duplicate-letter logic ----------

def test_repeated_letter_handling():
    corpus_test = ["speak", "speed", "spear"]
    result_hist = {"speed": "22200"}

    result = get_n_guesses(result_hist, corpus=corpus_test)
    assert "speed" not in result
    assert "speak" in result

def test_duplicate_letters_partial_match():
    # When a word has duplicate letters and only some are marked
    corpus_test = ["speed", "steel", "sleep", "creep", "peere"]
    
    # 'e' appears twice: first 'e' is wrong position (1), second 'e' is correct (2)
    result = get_n_guesses({"speed": "01210"}, corpus=corpus_test)
    
    for word in result:
        assert word.count('e') >= 2, f"{word} should have at least 2 'e's"
        assert word[2] == 'e', f"{word} should have 'e' at position 2"
        assert word[3] != 'e', f"{word} should not have 'e' at position 3"

def test_triple_letter_constraint():
    corpus_test = ["eerie", "eagle", "empty", "error", "eeres","eenlr"]
    
    # If we mark two 'e's as present but get '0' on others
    result = get_n_guesses({"eerie": "22100"}, corpus=corpus_test)
    for word in result:
        assert word.count('e') == 2, f"{word} should have exactly 2 'e's"
        assert word[0] == 'e' and word[1] == 'e'

def test_same_letter_different_positions():
    corpus_test = ["speed", "sleep", "sweep", "creep", "breed", "xyeze"]
    
    # 'e' at position 2 is correct, 'e' at position 3 is not
    result = get_n_guesses({"speed": "00210"}, corpus=corpus_test)
    
    for word in result:
        assert word[2] == 'e'
        assert word[3] != 'e'
        assert word.count('e') >= 2
