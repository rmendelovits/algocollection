from typing import Any, Mapping
from algocollection.common import Algorithm, DLogTime


class Gcd(Algorithm):
    """Find the greatest common divisor between two numbers a and b.
    Methods
    -------
    execute(self, param_dict: Mapping[str, Any]) -> Any:
        first, unpacks param_dict into a and b
        Return the largest integer k which divides both a and b
    Notes
    -----
    Time Complexity:
        Let n = len(a) + len(b) (length in base 2)
        T(n) = O(n)
    """
    def execute(self, param_dict: Mapping[str, Any]) -> Any:
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
