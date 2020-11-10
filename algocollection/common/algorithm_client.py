from typing import Any, Mapping
from .algorithm_invoker import AlgorithmInvoker
from algocollection.search import LinearSearch, BinarySearch
from algocollection.sort import InsertionSort, SelectionSort


class AlgorithmClient(object):
    """The CLIENT class"""
    def __init__(self) -> None:
        self._algorithm_invoker = AlgorithmInvoker()

    @property
    def algorithm_invoker(self):
        return self._algorithm_invoker

    def run(self, cmd: str, param_dict: Mapping[str, Any]) -> Any:
        cmd = cmd.strip().lower()
        if cmd == "linear_search":
            return self._algorithm_invoker.execute(LinearSearch, param_dict)
        elif cmd == "binary_search":
            return self._algorithm_invoker.execute(BinarySearch, param_dict)
        elif cmd == "insertion_sort":
            return self._algorithm_invoker.execute(InsertionSort, param_dict)
        elif cmd == "selection_sort":
            return self._algorithm_invoker.execute(SelectionSort, param_dict)
        else:
            raise ValueError("Could not find algorithm")
