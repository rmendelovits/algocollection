"""Unit tests for greatest common divisor."""

import pytest
from algocollection.maths import Gcd


@pytest.mark.parametrize("a, b, gcd", [
    (1, 1, 1),
    (3, 5, 1),
    (2, 4, 2),
    (12, 27, 3),
    (12, 32, 4),
    (12, 36, 12)])
def test_gcd(a, b, gcd):
    assert Gcd().execute({"a": a, "b": b}) == gcd
