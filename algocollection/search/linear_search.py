""" algocollection - a fun collection of algorithms
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

from algocollection.common import Algorithm, DLogTime, DTime


class LinearSearch(Algorithm):
    def execute(self, param_dict: Mapping[str, Any]) -> Any:
        """
        Finds the key in the given array by looking through the array
        starting from the first index one by one until it reaches
        the final element and doesn't find it and returns None, or
        finds the element and returns it's index in the array.

        Parameters
        ----------
        param_dict : dictionary containing all the parameters
        for the actual function
        param_dict['array'] : array
            1-D array of Any type which may or may not contain the key
        key : Any
            The value we are looking for in the array
        Returns
        -------
        out : None or int
            Returns the index of the key in the array, or None if the key
            is not in the array
        Examples
        --------
        >>> from algocollection.search import LinearSearch
        >>> primes = [2, 3, 5, 7, 11]
        >>> LinearSearch().execute({"array": primes, "key": 3})
        1
        >>> LinearSearch().execute({"array": primes, "key": 4})
        None
        """
        if ('array' not in param_dict or 'key' not in param_dict):
            raise ValueError("LinearSearch requires an array"
                             " and a key to execute")
        array = param_dict['array']
        key = param_dict['key']

        return self.run(array, key)

    def run(self, array, key):
        """
        Finds the key in the given array by looking through the array
        starting from the first index one by one until it reaches
        the final element and doesn't find it and returns None, or
        finds the element and returns it's index in the array.

        Parameters
        ----------
        array : array
            1-D array of Any type which may or may not contain the key
        key : Any
            The value we are looking for in the array
        Returns
        -------
        out : None or int
            Returns the index of the key in the array, or None if the key
            is not in the array
        Examples
        --------
        >>> from algocollection.search import LinearSearch
        >>> primes = [2, 3, 5, 7, 11]
        >>> LinearSearch().run(primes, 3)
        1
        >>> LinearSearch().run(primes, 4)
        None
        """
        for i in range(len(array)):
            if array[i] == key:
                return i
        return None

    def best_case_time_complexity(self):
        # Our key could be the first item we search
        return DLogTime.constant

    def average_case_time_complexity(self):
        # Our key could not be in the array, have to search whole array
        return DTime.linear

    def worst_case_time_complexity(self):
        # We expect it to be around halfway, which is just a constant
        # times linear time
        return DTime.linear

    def worst_case_space_complexity(self):
        # No space dependent variables needed
        return DLogTime.constant
