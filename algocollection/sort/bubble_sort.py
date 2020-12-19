""" algocollection - sort an array
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


class BubbleSort(Algorithm):
    """Sort the array from smallest to largest element
    Methods
    -------
    execute(self, param_dict) -> Any:
        first, unpacks param_dict into array
        Sort the array
    Notes
    -----
    Time Complexity:
        Let n = len(array)
        T(n) = O(n^2)
    """
    def execute(self, param_dict) -> Any:
        # unpack the param_dict
        if 'array' not in param_dict:
            raise ValueError("BubbleSort requires an array to execute")
        array = param_dict['array']

        # actual algorthm
        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        return array

    def best_case_time_complexity(self):
        return DTime.linear

    def average_case_time_complexity(self):
        return DTime.quadratic

    def worst_case_time_complexity(self):
        return DTime.quadratic

    def worst_case_space_complexity(self):
        return DLogTime.constant
