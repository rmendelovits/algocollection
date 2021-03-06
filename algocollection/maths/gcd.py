""" algocollection - find greatest common divisor
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

from algocollection.common import Algorithm, DLogTime


class Gcd(Algorithm):
    """Find the greatest common divisor between two numbers a and b.
    Methods
    -------
    execute(self, param_dict) -> Any:
        first, unpacks param_dict into a and b
        Return the largest integer k which divides both a and b
    Notes
    -----
    Time Complexity:
        Let n = len(a) + len(b) (length in base 2)
        T(n) = O(n)
    """
    def execute(self, param_dict) -> Any:
        # unpack the param_dict
        if ('a' not in param_dict or 'b' not in param_dict):
            raise ValueError("Gcd requires two integers a and b")
        a = param_dict['a']
        b = param_dict['b']

        # actual algorthm
        while b != 0:
            a, b = b, a % b
        return abs(a)

    def best_case_time_complexity(self):
        return DLogTime.constant

    def average_case_time_complexity(self):
        return DLogTime.logarithmic

    def worst_case_time_complexity(self):
        return DLogTime.logarithmic

    def worst_case_space_complexity(self):
        return DLogTime.constant
