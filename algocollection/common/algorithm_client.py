from typing import Any, Mapping
from .algorithm_invoker import AlgorithmInvoker
from algocollection.search import LinearSearch, BinarySearch
from algocollection.sort import BubbleSort, InsertionSort, MergeSort, QuickSort, SelectionSort
from algocollection.maths import Gcd, ExtendedGcd
from algocollection.graphs import BreadthFirstSearch, DepthFirstSearch, Dijkstra, Prim, Kruskal


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
        elif cmd == "merge_sort":
            return self._algorithm_invoker.execute(MergeSort, param_dict)
        elif cmd == "bubble_sort":
            return self._algorithm_invoker.execute(BubbleSort, param_dict)
        elif cmd == "quick_sort":
            return self._algorithm_invoker.execute(QuickSort, param_dict)
        elif cmd == "gcd":
            return self._algorithm_invoker.execute(Gcd, param_dict)
        elif cmd == "extended_gcd":
            return self._algorithm_invoker.execute(ExtendedGcd, param_dict)
        elif cmd == "breadth_first_search":
            return self._algorithm_invoker.execute(BreadthFirstSearch, param_dict)
        elif cmd == "depth_first_search":
            return self._algorithm_invoker.execute(DepthFirstSearch, param_dict)
        elif cmd == "dijkstra":
            return self._algorithm_invoker.execute(Dijkstra, param_dict)
        elif cmd == "prim":
            return self._algorithm_invoker.execute(Prim, param_dict)
        elif cmd == "kruskal":
            return self._algorithm_invoker.execute(Kruskal, param_dict)
        else:
            raise ValueError("Could not find algorithm")
