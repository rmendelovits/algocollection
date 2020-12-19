""" algocollection - Metaclass for algorithm interface
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

from abc import ABC, abstractmethod
from typing import Any, Mapping


class Algorithm(ABC):
    """The COMMAND interface"""

    @abstractmethod
    def execute(self, param_dict) -> Any:
        pass

    @abstractmethod
    def best_case_time_complexity(self):
        pass

    @abstractmethod
    def average_case_time_complexity(self):
        pass

    @abstractmethod
    def worst_case_time_complexity(self):
        pass

    @abstractmethod
    def worst_case_space_complexity(self):
        pass
