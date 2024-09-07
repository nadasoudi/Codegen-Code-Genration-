def find_close_matches(input_string, possibilities, n=3, cutoff=0.7):
    """
    :param input_string: str, the input string
    :param possibilities: list, a list of strings
    :param n: int, the number of strings to find
    :param cutoff: float, the minimum length of a match
    :return: list, a list of strings
    """
    if len(input_string) < n:
        return []
    if