from typing import Any, Mapping
from algocollection.common import Algorithm


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
