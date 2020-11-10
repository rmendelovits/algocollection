from typing import Any, Mapping
from .algorithm_invoker import AlgorithmInvoker
from algocollection.search import LinearSearch, BinarySearch


class AlgorithmClient(object):
    """The CLIENT class"""
    def __init__(self) -> None:
        self._algorithm_invoker = AlgorithmInvoker()

    @property
    def algorithm_invoker(self):
        return self._algorithm_invoker

    def run(self, cmd: str, param_dict: Mapping[str, Any]) -> Any:
        cmd = cmd.strip().upper()
        if cmd == "LINEARSEARCH":
            return self._algorithm_invoker.execute(LinearSearch, param_dict)
        elif cmd == "BINARYSEARCH":
            return self._algorithm_invoker.execute(BinarySearch, param_dict)
        else:
            raise ValueError("Could not find algorithm")
