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
    >>> border_array("abaabaa")
    [0, 0, 1, 1, 2, 3, 4]
    >>> border_array("abcabdabcabc")
    [0, 0, 0, 1, 2, 0, 1, 2, 3, 4, 5, 3]
    """
    if x=="":
        return []
    border_list = [0 for _ in x]
    for i, c in enumerate(x):
        border_index = i
        while True:
            if border_index == 0:
                # border_list[i] = 0 # The list was initialized with zeros
                break
            previousBorder = border_list[border_index-1]
            if c == x[previousBorder]:
                border_list[i] = previousBorder+1
                break
            # We go backwards throughout the border
            border_index = previousBorder
    return border_list


def strict_border_array(x: str) -> list[int]:
    """
    Construct the strict border array for x.

    A strict border array is one where the border cannot
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
    >>> strict_border_array("abaabaa")
    [0, 0, 1, 0, 0, 1, 4]
    >>> strict_border_array("abcabdabcabc")
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 5, 3]
    """
    ba = border_array(x)
    bax = [0 for _ in x]

    for i, bai in enumerate(ba[:len(ba)-1]):
        if bai == 0:
            bax[i] = 0
        elif x[i+1] != x[bai]:
            bax[i] = bai
        else:
            bax[i] = bax[bai-1]
    
    bax[len(ba)-1] = ba[len(ba)-1]
    return bax

print(border_array("abcabdabcabc"))