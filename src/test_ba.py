# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

import string
import random
from ba import (
    border_array,
    strict_border_array
)


def random_string(n: int, alpha: str = string.ascii_uppercase) -> str:
    """Create a random string."""
    return ''.join(random.choices(alpha, k=n))


def fibonacci_string(n: int) -> str:
    """Fibonacci string n; has length Fib(n+2)."""
    a, b = "a", "ab"
    for _ in range(n):
        a, b = b, a + b
    return b


def test_is_border(x: str, b: int, i: int) -> None:
    """Brute force checks if x[:b] is a border of x[:i+1]."""
    assert x[:b] == x[i-b+1:i+1], "We have a border"


def test_is_strict_border(x: str, b: int, i: int) -> None:
    """Checks if x[:b] is a border of x[:i+1] and that it is strict."""
    test_is_border(x, b, i)
    assert b == 0 or i == len(x) - 1 or x[b] != x[i+1], \
        "The border is strict"


def test_border_array() -> None:
    """Test the border_array function."""
    for _ in range(10):
        x = random_string(20, "acgt")
        ba = border_array(x)
        for i, b in enumerate(ba):
            test_is_border(x, b, i)
    for k in range(3, 7):
        x = fibonacci_string(k)
        ba = border_array(x)
        for i, b in enumerate(ba):
            test_is_border(x, b, i)


def test_strict_border_array() -> None:
    """Test the strict_border_array function."""
    for _ in range(10):
        x = random_string(20, "acgt")
        ba = strict_border_array(x)
        for i, b in enumerate(ba):
            test_is_strict_border(x, b, i)
    for k in range(3, 7):
        x = fibonacci_string(k)
        ba = strict_border_array(x)
        for i, b in enumerate(ba):
            test_is_strict_border(x, b, i)
