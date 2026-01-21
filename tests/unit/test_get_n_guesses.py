import pytest
from wordguess.get_n_guesses import get_n_guesses
from wordguess._internals import minidict

# Claude Sonnet4.5 was used to generate sample result_hist dictionaries for various cases
# and write assert statements for lengthier cases


def test_invalid_result_histories():
    """Checking Invalid Input type for result history throws error"""
    # ---------- Invalid input structure ----------
    with pytest.raises(TypeError):
        get_n_guesses(["hello", "10001"])

    with pytest.raises(TypeError):
        get_n_guesses({"hello": 10010})

    with pytest.raises(ValueError):
        get_n_guesses({"hello": "100001"})

    # not present in corpus
    with pytest.raises(ValueError):
        get_n_guesses({"zxcnw": "00100"})

    with pytest.raises(ValueError):
        get_n_guesses({"hello": "12300"})


# ---------- Consistency conflicts ----------


def test_result_history_conflicts():
    """Checking conflicting result histories throw error"""
    # ---------- Conflict 2 to 1 ----------
    with pytest.raises(ValueError):
        get_n_guesses({"under": "00200", "index": "00100"})

    # ---------- Conflict 1 to 2-----------
    with pytest.raises(ValueError):
        get_n_guesses({"about": "10000", "angle": "20000"})

    # ---------- Conflict 2 to 0 ----------
    with pytest.raises(ValueError):
        get_n_guesses({"about": "20000", "angle": "02000"})

    # ---------- Conflict 0 to 2 -----------
    with pytest.raises(ValueError):
        get_n_guesses({"about": "00000", "angle": "20000"})

    # ---------- Conflict 1 to 0 -----------
    with pytest.raises(ValueError):
        get_n_guesses({"about": "10000", "angle": "00000"})

    # ---------- Conflict 0 to 1 -----------
    with pytest.raises(ValueError):
        get_n_guesses({"about": "00000", "angle": "10000"})

    # ------ two letters on same position ----------
    with pytest.raises(ValueError):
        get_n_guesses({"about": "02000", "angle": "02000"})

    # ------ too many letters present ----------
    # only 1s
    with pytest.raises(ValueError):
        get_n_guesses({"about": "11111", "angle": "11000"})
    # 1s and 2s
    with pytest.raises(ValueError):
        get_n_guesses({"about": "11211", "angle": "11000"})


# ---------- Basic filtering behavior ----------


def test_empty_history_returns_all():
    """Checking unconstrained case returns all possible values"""
    # returns whole corpus for empty history
    result = get_n_guesses({}, corpus=minidict)
    assert set(result) == set(minidict)


def test_single_zero_constraint():
    """Checking case with all 0's"""
    result = get_n_guesses({"crane": "00000"}, corpus=minidict)
    for word in result:
        assert "c" not in word
        assert "r" not in word
        assert "a" not in word
        assert "n" not in word
        assert "e" not in word


def test_correct_position_constraint():
    """Checking case with one 2"""
    result = get_n_guesses({"crane": "20000"}, corpus=minidict)
    for word in result:
        assert word[0] == "c", f"Word {word} doesn't have 'c' at position 0"


def test_wrong_position_constraint():
    """Checking case with one 1"""
    result = get_n_guesses({"crane": "10000"}, corpus=minidict)
    for word in result:
        assert "c" in word, f"Word {word} doesn't contain 'c'"
        assert word[0] != "c", f"Word {word} has 'c' at position 0"


def test_correct_word_guesses():
    """Checking case with all 2's does not suggest anything"""
    result = get_n_guesses({"crane": "22222"}, corpus=minidict)
    assert result == []


def test_target_outside_corpus():
    """Checking case when target is not guessed but no valid answer is left in corpus"""
    with pytest.raises(ValueError):
        get_n_guesses({"crane": "22211"}, corpus=minidict)


# ---------- Multiple constraints ----------


def test_multiple_guess_constraints():
    """Checking regular use case with many constraints"""
    result_hist = {"repay": "10000", "print": "01001", "motor": "02101"}

    result = get_n_guesses(result_hist, corpus=minidict)

    for word in result:
        assert "r" in word
        assert word[0] != "r"
        assert "e" not in word
        assert "p" not in word
        assert "a" not in word
        assert "y" not in word

        assert word[1] != "r"
        assert "i" not in word
        assert "n" not in word
        assert "t" in word
        assert word[4] != "t"

        assert "m" not in word
        assert word[1] == "o"
        assert word[2] != "t"
        assert word[3] != "o"

        assert word.count("o") == 1

    # checking already guessed words arent present
    assert "repay" not in result
    assert "print" not in result
    assert "motor" not in result


# ---------- n parameter behavior ----------


def test_n_parameter():
    """Checking different values of n and wrong input types of n"""
    assert len(get_n_guesses({}, n=10, corpus=minidict)) == 10
    assert len(get_n_guesses({}, n=1, corpus=minidict)) == 1

    with pytest.raises(TypeError):
        get_n_guesses({}, n=1.0)
    with pytest.raises(TypeError):
        get_n_guesses({}, n=-1)


# ---------- Duplicate-letter logic ----------


def test_repeated_letter_handling():
    """
    Checking edge cases where duplicate letters are present in result hist
    Case where one letter is 2 and one is 0
    """
    corpus_test = ["speak", "speed", "spear"]
    result_hist = {"speed": "22200"}

    result = get_n_guesses(result_hist, corpus=corpus_test)
    assert "speed" not in result
    assert "speak" in result


def test_duplicate_letters_partial_match():
    """
    Checking edge cases where duplicate letters are present in result hist
    Case where one letter is 2 and one is 1
    """
    corpus_test = ["speed", "steel", "sleep", "creep", "peere"]

    result = get_n_guesses({"speed": "01210"}, corpus=corpus_test)

    for word in result:
        assert word.count("e") >= 2, f"{word} should have at least 2 'e's"
        assert word[2] == "e", f"{word} should have 'e' at position 2"
        assert word[3] != "e", f"{word} should not have 'e' at position 3"


def test_same_letter_different_positions():
    """
    Checking edge cases where duplicate letters are present in result hist
    Case where one letter is 1 and one is 0
    """
    corpus_test = ["speed", "sleep", "sweep", "creep", "breed", "xyzea"]

    result = get_n_guesses({"speed": "00100"}, corpus=corpus_test)

    for word in result:
        assert word[2] != "e"
        assert word.count("e") == 1


def test_triple_letter_constraint():
    """
    Checking edge cases where triple letters are present in result hist
    Case where two letters are 2 and one is 0
    """
    corpus_test = ["eerie", "eagle", "empty", "error", "eeres", "eenlr"]

    result = get_n_guesses({"eerie": "22100"}, corpus=corpus_test)
    for word in result:
        assert word.count("e") == 2, f"{word} should have exactly 2 'e's"
        assert word[0] == "e" and word[1] == "e"
