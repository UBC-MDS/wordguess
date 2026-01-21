import pytest
from wordguess.get_result import get_result


@pytest.fixture
def mock_corpus():
    """A small fixture to act as our dictionary."""
    return ["apple", "apply", "stare", "tears", "abort", "alarm", "books", "slope"]


def test_get_result_value_errors(mock_corpus):
    """Test that ValueErrors are raised for length mismatch or invalid words."""
    with pytest.raises(ValueError, match="same length"):
        get_result("apple", "longword", corpus=mock_corpus)

    with pytest.raises(ValueError, match="not a valid word"):
        get_result("apple", "zzzzz", corpus=mock_corpus)

    with pytest.raises(ValueError, match="not a valid word"):
        get_result("zzzzz", "apple", corpus=mock_corpus)


def test_get_result_type_errors():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="must be strings"):
        get_result("apple", 12345)

    with pytest.raises(TypeError, match="must be strings"):
        get_result(None, "apple")


def test_get_result(mock_corpus):
    """Test standard inputs."""
    # Test with some matches
    assert get_result("apple", "apply", corpus=mock_corpus) == "22220"
    assert get_result("stare", "tears", corpus=mock_corpus) == "11221"

    # Test with no matches
    custom_corpus = ["apple", "mxxxx"]
    assert get_result("apple", "mxxxx", corpus=custom_corpus) == "00000"

    # Test with repeated letters
    assert get_result("abort", "alarm", corpus=mock_corpus) == "20020"
