def result_to_pattern(result: str) -> str:
    """
    Convert a result string to a human-readable pattern of symbols.

    This function maps each character in a result string to a corresponding colored square
    symbol.
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
    str: The corresponding human-readable string pattern composed of UTF-8 colored symbols.

    See Also
    --------
    get_result : A function that generate the result string for a given guess against a target word.

    Example:
    >>> result_to_pattern("01102")
    "⬛🟨🟨⬛🟩"
    >>> result_to_pattern("0001221")
    "⬛⬛⬛🟨🟩🟩🟨"
    """
    pattern_dict = {'0': "\u2B1B",
                    '1': "\U0001F7E8",
                    '2': "\U0001F7E9"}
    pattern = ""
    for char in result:
        pattern += pattern_dict[char]
    
    return pattern