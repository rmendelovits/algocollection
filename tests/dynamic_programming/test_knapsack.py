"""Unit tests for fractional knapsack."""

import pytest
from algocollection.dynamic_programming import Knapsack


@pytest.mark.parametrize("weights, values, capacity, knapsack", [
    ([], [], 1, 0),
    ([2], [1], 1, 0.5),
    ([2], [1], 2, 1),
    ([1, 7, 100, 4, 3], [100, 21, 50, 2, 25], 6, 131)])
def test_0_1_knapsack(weights, values, capacity, knapsack):
    assert Knapsack().execute({"weights": weights,
                               "values": values,
                               "capacity": capacity}) == knapsack
