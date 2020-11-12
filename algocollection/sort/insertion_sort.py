from typing import Any, Mapping
from algocollection.common import Algorithm, DLogTime, DTime


class InsertionSort(Algorithm):
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
        T(n) = O(n^2)
    """
    def execute(self, param_dict: Mapping[str, Any]) -> Any:
        # unpack the param_dict
        if 'array' not in param_dict:
            raise ValueError("InsertionSort requires an array to execute")
        array = param_dict['array']

        # actual algorthm
        for i in range(len(array) - 1):
            j = i
            current_element = array[j + 1]

            while j >= 0 and current_element < array[j] :
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = current_element
        return array

    def best_case_time_complexity(self):
        return DTime.linear

    def average_case_time_complexity(self):
        return DTime.quadratic

    def worst_case_time_complexity(self):
        return DTime.quadratic

    def worst_case_space_complexity(self):
        return DLogTime.constant
