"""Unit tests for fractional knapsack."""

import pytest
from algocollection.greedy import JobScheduling


@pytest.mark.parametrize("starts, ends, optimal_num_of_jobs", [
    ([], [], 0),
    ([1, 2], [2, 3], 2),
    ([1, 2], [3, 4], 1),
    ([1, 7, 100, 4, 12], [100, 21, 150, 12, 13], 3)])
def test_unweighted_job_scheduling(starts, ends, optimal_num_of_jobs):
    assert JobScheduling().execute({"starts": starts,
                                    "ends": ends}) == optimal_num_of_jobs
