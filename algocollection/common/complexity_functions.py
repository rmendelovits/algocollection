""" algocollection - enums for algorithm timing
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

from enum import Enum


class DLogTime(Enum):
    constant = 0  # O(1)
    logarithmic = 1  # O(log n)


class DTime(Enum):
    linear = 2  # O(n)
    linearithmic = 3  # O(n log n)
    quadratic = 4  # O(n^2)


class GraphTime(Enum):
    elogv = 1234501
