"""Module for computing border arrays."""


def border_array(x: str) -> list[int]:
    """
    Construct the border array for x.

    >>> border_array("aaba")
    [0, 1, 0, 1]
    >>> border_array("ississippi")
    [0, 0, 0, 1, 2, 3, 4, 0, 0, 1]
    >>> border_array("")
    []
    """
    return []  # FIXME


def strict_border_array(x: str) -> list[int]:
    """
    Construct the strict border array for x.

    A struct border array is one where the border cannot
    match on the next character. If b is the length of the
    longest border for x[:i+1], it means x[:b] == x[i-b:i+1],
    but for a strict border, it must be the longest border
    such that x[b] != x[i+1].

    >>> strict_border_array("aaba")
    [0, 1, 0, 1]
    >>> strict_border_array("aaaba")
    [0, 0, 2, 0, 1]
    >>> strict_border_array("ississippi")
    [0, 0, 0, 0, 0, 0, 4, 0, 0, 1]
    >>> strict_border_array("")
    []
    """
    return []  # FIXME
