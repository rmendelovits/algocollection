from typing import Any, Mapping
from algocollection.common import Algorithm, DLogTime, DTime


class QuickSort(Algorithm):
    """Sort the array from smallest to largest element
    Methods
    -------
    execute(self, param_dict: Mapping[str, Any]) -> Any:
        first, unpacks param_dict into array
        Sort the array
    Notes
    -----
    Time Complexity:
        Let n = len(array)
        T(n) = O(n * log_2(n))
    """
    def execute(self, param_dict: Mapping[str, Any]) -> Any:
        # unpack the param_dict
        if 'array' not in param_dict:
            raise ValueError("QuickSort requires an array to execute")
        array = param_dict['array']

        # call our recursive algorithm with default parameters
        return self.quick_sort(array)

    def quick_sort(self, array):
        if len(array) < 2:
            return array
        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

    def best_case_time_complexity(self):
        return DTime.linearithmic

    def average_case_time_complexity(self):
        return DTime.linearithmic

    def worst_case_time_complexity(self):
        return DTime.quadratic

    def worst_case_space_complexity(self):
        return DLogTime.logarithmic
