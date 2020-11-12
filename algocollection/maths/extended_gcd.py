from typing import Any, Mapping
from algocollection.common import Algorithm, DLogTime


class ExtendedGcd(Algorithm):
    """ Find two integers q and r such that a * q + b * r = GCD(a, b)
    and q, r are both co-prime.
    Methods
    -------
    execute(self, param_dict: Mapping[str, Any]) -> Any:
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
    def execute(self, param_dict: Mapping[str, Any]) -> Any:
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
