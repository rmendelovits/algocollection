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


class LinearSearch(Algorithm):
    """An implimentation of the linear search algorithm.
    Methods
    -------
    execute(self, param_dict: Mapping[str, Any]) -> Any:
        first, unpacks param_dict into array and key
        Search the array for a key
            If the key is found, return the index in the array
                (from 0 to len(array) - 1)
            Otherwise return None
    Notes
    -----
    Time Complexity:
        Let n = len(array)
        T(n) = O(n)
    """
    def execute(self, param_dict: Mapping[str, Any]) -> Any:
        # unpack the param_dict
        if ('array' not in param_dict or 'key' not in param_dict):
            raise ValueError("LinearSearch requires an array"
                             " and a key to execute")
        array = param_dict['array']
        key = param_dict['key']

        # actual algorthm
        for i in range(len(array)):
            if array[i] == key:
                return i
        return None

    def best_case_time_complexity(self):
        return DLogTime.constant

    def average_case_time_complexity(self):
        return DTime.linear

    def worst_case_time_complexity(self):
        return DTime.linear

    def worst_case_space_complexity(self):
        return DLogTime.constant
