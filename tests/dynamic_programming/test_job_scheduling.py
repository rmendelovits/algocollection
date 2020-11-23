"""Unit tests for fractional knapsack."""

import pytest
from algocollection.dynamic_programming import JobScheduling


@pytest.mark.parametrize("starts, ends, weights, optimal_num_of_jobs", [
    ([], [], [], 0),
    ([1, 2], [2, 3], [1, 2], 3),
    ([1, 2], [3, 4], [1, 2], 2),
    ([1, 7, 100, 4, 12], [100, 21, 150, 12, 13], [1, 2, 3, 4, 5], 3)])
def test_unweighted_job_scheduling(starts,
                                   ends,
                                   weights,
                                   optimal_num_of_jobs):
    assert JobScheduling().execute({"starts": starts,
                                    "ends": ends,
                                    "weights": weights}) == optimal_num_of_jobs
