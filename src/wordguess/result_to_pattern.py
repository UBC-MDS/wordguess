def result_to_pattern(result: str) -> str:
    """
    Convert a result string to a human-readable pattern of symbols.

    This function maps each character in a result string to a corresponding colored square symbol.
    
    - The character '0' maps to a dark grey square symbol,
    - The character '1' maps to a yellow square symbol and,
    - The character '2' maps to a green square symbol.
    
    The output is a string composed of UTF-8 colored square symbols.

    Parameters
    ----------
    result : str
        A string consisting only of the '0', '1' or '2' characters.

    Returns
    -------
    str
        The corresponding human-readable string pattern composed of UTF-8 colored symbols.

    Raises
    ------
    TypeError
        If result is not of type str.
    ValueError
        If result contains characters other than '0', '1' and '2'.

    See Also
    --------
    get_result : A function that generate the result string for a given guess against a target word.

    Examples
    --------
    >>> result_to_pattern("01102")
    '⬛🟨🟨⬛🟩'
    >>> result_to_pattern("0001221")
    '⬛⬛⬛🟨🟩🟩🟨'
    """
    if not isinstance(result, str):  # checks that input is of `str` type
        raise TypeError(f"Expected the input to be of type str, got {type(result)}")

    allowed_chars = {"0", "1", "2"}  # only characters allowed in input string
    invalid_chars = set(result) - allowed_chars
    if invalid_chars:  # checks if there are other characters in result
        raise ValueError(
            f"Input contains invalid characters: {''.join(sorted(invalid_chars))}"
        )
    pattern_dict = {"0": "\u2b1b", "1": "\U0001f7e8", "2": "\U0001f7e9"}
    return "".join(pattern_dict[char] for char in result)
