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
from algocollection.helpers import KnapsackItem


class Knapsack(Algorithm):
    """Given a list of items with weights and values,
    pack the maximal amount of items weighing no more than capacity
    Methods
    -------
    execute(self, param_dict: Mapping[str, Any]) -> Any:
        first, unpacks param_dict into weights, values, and capacity
        Sort the items in decreasing order of value per cost
        While capacity would not be reached, add all of next item
        then add a much of current item to meet capacity
    Notes
    -----
    Time Complexity:
        Let n = len(weights)
        T(n) = O(n * log_2(n))
    """
    def execute(self, param_dict: Mapping[str, Any]) -> Any:
        # unpack the param_dict
        if ('weights' not in param_dict
            or 'values' not in param_dict
                or 'capacity' not in param_dict):
            raise ValueError("knapsack requires weights, values"
                             " and the capacity to execute")
        weights = param_dict['weights']
        values = param_dict['values']
        capacity = param_dict['capacity']
        if len(weights) != len(values):
            raise ValueError("weights and values must be same len")

        # actual algorthm
        optimal_matrix = [[0 for i in range(capacity + 1)]
                          for j in range(len(weights) + 1)]
        for i in range(1, len(weights) + 1):
            for j in range(1, capacity + 1):
                if weights[i - 1] <= j:
                    optimal_matrix[i][j] = max(values[i - 1] +
                                               optimal_matrix[i - 1]
                                               [j - weights[i - 1]],
                                               optimal_matrix[i - 1][j])
                else:
                    optimal_matrix[i][j] = optimal_matrix[i - 1][j]
        return optimal_matrix[len(weights)][capacity]

    def best_case_time_complexity(self):
        return DTime.linearithmic

    def average_case_time_complexity(self):
        return DTime.linearithmic

    def worst_case_time_complexity(self):
        return DTime.linearithmic

    def worst_case_space_complexity(self):
        return DLogTime.linear
