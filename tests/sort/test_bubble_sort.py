"""Unit tests for selection sort."""

import pytest
from algocollection.sort import BubbleSort

primes = [73, 13, 43, 47, 83, 97, 71, 79, 17, 19, 3, 37,
          41, 61, 67, 5, 23, 7, 89, 11, 29, 31, 2, 59, 53]


@pytest.mark.parametrize("array", [
    ([]),
    (["exists"]),
    (["exists", "also exists"]),
    (primes)])
def test_bubble_sort(array):
    assert BubbleSort().execute({"array": array}) == sorted(array)
