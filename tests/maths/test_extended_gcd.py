"""Unit tests for greatest common divisor."""

from algocollection.maths import ExtendedGcd

import pytest

@pytest.mark.parametrize("a, b, gcd_triple", [
    (1, 1, (1, 0, 1)),
    (3, 5, (1, 2, -1)),
    (2, 4, (2, 1, 0)),
    (12, 27, (3, -2, 1)),
    (12, 32, (4, 3, -1)),
    (12, 36, (12, 1, 0))])
def test_extended_gcd(a, b, gcd_triple):
    assert ExtendedGcd().execute({"a": a, "b": b}) == gcd_triple
