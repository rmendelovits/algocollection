from abc import ABC, abstractmethod
from typing import Any, Mapping


class Algorithm(ABC):
    """The COMMAND interface"""

    @abstractmethod
    def execute(self, param_dict: Mapping[str, Any]) -> Any:
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
