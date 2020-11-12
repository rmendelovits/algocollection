from typing import Any, Mapping
from algocollection.common import Algorithm, DLogTime, DTime


class MergeSort(Algorithm):
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
            raise ValueError("MergeSort requires an array to execute")
        array = param_dict['array']

        # call our recursive algorithm with default parameters
        return self.merge_sort(array)

    def merge_sort(self, array):
        if len(array) < 2:
            return array
        left_array = array[0:len(array)//2]
        right_array = array[len(array)//2:]
        left_array = self.merge_sort(left_array)
        right_array = self.merge_sort(right_array)
        return self.merge(left_array, right_array)

    def merge(self, left_array, right_array):
        left_current_index = 0
        right_current_index = 0
        sorted_array = []
        while (left_current_index < len(left_array)
               and right_current_index < len(right_array)):
            if (left_array[left_current_index]
               > right_array[right_current_index]):
                sorted_array.append(right_array[right_current_index])
                right_current_index += 1
            else:
                sorted_array.append(left_array[left_current_index])
                left_current_index += 1
        sorted_array += left_array[left_current_index:]
        sorted_array += right_array[right_current_index:]
        return sorted_array

    def best_case_time_complexity(self):
        return DTime.linearithmic

    def average_case_time_complexity(self):
        return DTime.linearithmic

    def worst_case_time_complexity(self):
        return DTime.linearithmic

    def worst_case_space_complexity(self):
        return DLogTime.logarithmic
