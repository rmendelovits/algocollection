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

from algocollection.common import Algorithm, DLogTime


class BinarySearch(Algorithm):

    def execute(self, param_dict) -> Any:
        """
        Finds the key in the given array by looking through the array
        dividing the search space by half by eliminating items
        either lower or higher than it.
        This function either doesn't find the key and returns None, or
        finds the element and returns it's index in the array.

        Parameters
        ----------
        param_dict : dictionary containing all the parameters
        for the actual function
        param_dict['array'] : array
            1-D array of Any type which may or may not contain the key
        param_dict['key'] : Any
            The value we are looking for in the array
        Returns
        -------
        out : None or int
            Returns the index of the key in the array, or None if the key
            is not in the array
        Examples
        --------
        >>> from algocollection.search import BinarySearch
        >>> primes = [2, 3, 5, 7, 11]
        >>> BinarySearch().execute({"array": primes, "key": 3})
        1
        >>> BinarySearch().execute({"array": primes, "key": 4})
        None
        """
        if ('array' not in param_dict or 'key' not in param_dict):
            raise ValueError("BinarySearch requires an array"
                             " and a key to execute")
        array = param_dict['array']
        key = param_dict['key']

        return self.run(array, key)

    def run(self, array, key):
        """
        Finds the key in the given array by looking through the array
        dividing the search space by half by eliminating items
        either lower or higher than it.
        This function either doesn't find the key and returns None, or
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
        >>> from algocollection.search import BinarySearch
        >>> primes = [2, 3, 5, 7, 11]
        >>> BinarySearch().run(primes, 3)
        1
        >>> BinarySearch().run(primes, 4)
        None
        """
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

    def best_case_time_complexity(self):
        # Our key could be the first item we search
        return DLogTime.constant

    def average_case_time_complexity(self):
        # most elements fall under the worst case analysis
        return DLogTime.logarithmic

    def worst_case_time_complexity(self):
        # every element can be searched in logarithmic time
        return DLogTime.logarithmic

    def worst_case_space_complexity(self):
        # No space dependent variables needed
        return DLogTime.constant
