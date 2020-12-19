""" algocollection - linear search for element in array
    Copyright (C) 2020 Raymond Mendelovits

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>. """

from typing import Any, Mapping

from algocollection.common import Algorithm, DLogTime, DTime
from algocollection.helpers import Job


class JobScheduling(Algorithm):
    """Given a list of items with start and end times (positive),
    return the maximum number of non conflicting jobs
    Methods
    -------
    execute(self, param_dict) -> Any:
        first, unpacks param_dict into starts, ends
        Sort the items in increasing order of end time
        For each job, add it if it doesn't conflict
    Notes
    -----
    Time Complexity:
        Let n = len(weights)
        T(n) = O(n * log_2(n))
    """
    def execute(self, param_dict) -> Any:
        # unpack the param_dict
        if ('starts' not in param_dict
                or 'ends' not in param_dict):
            raise ValueError("JobScheduling requires starts, ends"
                             " to execute")
        starts = param_dict['starts']
        ends = param_dict['ends']
        if len(starts) != len(ends):
            raise ValueError("starts and ends must be same len")

        # actual algorthm
        jobs = []
        number_of_selected_jobs = 0
        for i in range(len(starts)):
            jobs.append(Job(starts[i], ends[i]))
        jobs.sort()
        current_time = 0
        for job in jobs:
            if job.start >= current_time:
                current_time = job.end
                number_of_selected_jobs += 1
        return number_of_selected_jobs

    def best_case_time_complexity(self):
        return DTime.linearithmic

    def average_case_time_complexity(self):
        return DTime.linearithmic

    def worst_case_time_complexity(self):
        return DTime.linearithmic

    def worst_case_space_complexity(self):
        return DLogTime.linear
