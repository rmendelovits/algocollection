""" algocollection - find greatest common divisor and coefficients
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


class ExtendedGcd(Algorithm):
    """ Find two integers q and r such that a * q + b * r = GCD(a, b)
    and q, r are both co-prime.
    Methods
    -------
    execute(self, param_dict) -> Any:
        first, unpacks param_dict into a and b
        Return a triple (g, q, r)
        such that g is the largest integer which divides both a and b
        and g can be written as aq + br = g
    Notes
    -----
    Time Complexity:
        Let n = len(array)
        T(n) = O(n)
    """
    def execute(self, param_dict) -> Any:
        # unpack the param_dict
        if ('a' not in param_dict or 'b' not in param_dict):
            raise ValueError("ExtendedGcd requires two integers a and b")
        a = param_dict['a']
        b = param_dict['b']

        # call our recursive algorithm with default parameters
        return self.extended_gcd(a, b)

    def extended_gcd(self, a, b):
        if (b == 0):
            return (a, 1, 0)
        else:
            (g, m, n) = self.extended_gcd(b, a % b)
            return (g, n, m - (a // b) * n)

    def best_case_time_complexity(self):
        return DLogTime.constant

    def average_case_time_complexity(self):
        return DLogTime.logarithmic

    def worst_case_time_complexity(self):
        return DLogTime.logarithmic

    def worst_case_space_complexity(self):
        return DLogTime.constant
