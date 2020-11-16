"""Unit tests for linear search."""

import pytest
from algocollection.search import BinarySearch

primes = [2, 3, 5, 7, 11]


@pytest.mark.parametrize("array, key, key_location", [
    ([], 0, None),
    (["exists"], "exists", 0),
    (["exists"], "does not exist", None),
    (primes, 2, 0),
    (primes, 7, 3),
    (primes, 6, None)])
def test_binary_search(array, key, key_location):
    assert BinarySearch().execute({"array": array, "key": key}) == key_location
