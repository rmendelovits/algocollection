from typing import Any, Mapping
from common import Algorithm

class BinarySearch(Algorithm):
    """Search the sorted array for a key
        If the key is found, return the index in the array
            (from 0 to len(array) - 1)
        Otherwise return None

    Time Complexity:
        Let n = len(array)
        T(n) = O(log_2(n))

    Keyword arguments:
    array -- The array you want to use to search for the key
    key -- The value you want to search for in the array
    """
    def execute(self, param_dict: Mapping[str, Any]) -> Any:
        # unpack the param_dict
        if (not 'array' in param_dict
            or not 'key' in param_dict):
            raise ValueError("LinearSearch requires an array"
            " and a key to execute")
        array = param_dict['array']
        key = param_dict['key']

        # actual algorthm
        left = 0
        right = len(array) - 1

        while left <= right:
            mid = left + (right - left) // 2
            current = array[mid]
            if current == key:
                return mid
            elif key >= current:
                left = mid + 1
            else:
                right = mid - 1
        return None
