from typing import Any, Mapping
from algocollection.common import Algorithm


class BubbleSort(Algorithm):
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
            raise ValueError("BubbleSort requires an array to execute")
        array = param_dict['array']

        # actual algorthm
        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                if array[j] > array[j+1] :
                    array[j], array[j+1] = array[j+1], array[j]
        return array
