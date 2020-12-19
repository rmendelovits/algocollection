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


class InsertionSort(Algorithm):
    def execute(self, param_dict) -> Any:
        """
        Sort the array from smallest to largest element

        Parameters
        ----------
        param_dict : dictionary containing all the parameters
        for the actual function
        param_dict['array'] : array
            1-D array of sortable elements
        Returns
        -------
        out : None or 1-D array
            Returns the array passed in sorted in increasing order
        Examples
        --------
        >>> from algocollection.sort import InsertionSort
        >>> primes = [7, 3, 11, 2, 5]
        >>> InsertionSort().execute({"array": primes})
        [2, 3, 5, 7, 11]
        >>> InsertionSort().execute({"array": [3, 2, 1]})
        [1, 2, 3]
        """
        # unpack the param_dict
        if 'array' not in param_dict:
            raise ValueError("InsertionSort requires an array to execute")
        array = param_dict['array']

        return self.run(array)

    def run(self, array):
        """
        Sort the array from smallest to largest element

        Parameters
        ----------
        array : array
            1-D array of Any type which may or may not contain the key
        Returns
        -------
        out : None or 1-D array
            Returns the array passed in sorted in increasing order
        Examples
        --------
        >>> from algocollection.sort import InsertionSort
        >>> primes = [7, 3, 11, 2, 5]
        >>> InsertionSort().sort(primes)
        [2, 3, 5, 7, 11]
        >>> InsertionSort().sort([3, 2, 1])
        [1, 2, 3]
        """
        for i in range(len(array) - 1):
            j = i
            current_element = array[j + 1]

            while j >= 0 and current_element < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = current_element
        return array

    def best_case_time_complexity(self):
        # The list is already sorted
        return DTime.linear

    def average_case_time_complexity(self):
        # every element needs to be moved a lot
        return DTime.quadratic

    def worst_case_time_complexity(self):
        # reserved sorted
        return DTime.quadratic

    def worst_case_space_complexity(self):
        # sorting can be done in place
        return DLogTime.constant
