"""Unit tests for greatest common divisor."""

from algocollection.graphs import Dijkstra

import pytest
import math

single_node_graph = {'S': set()}

connected_graph = {'S': {'B': 10, 'C': 1, 'F': 1},
         'B': {'S': 10, 'D': 1, 'E': 1, 'T': 1},
         'C': {'S': 1, 'F': 1},
         'D': {'B': 1},
         'E': {'B': 1, 'F': 1},
         'F': {'S': 1, 'C': 1, 'E': 1},
         'T': {'B': 1}}

disconnected_graph = {'S': {'B': 10, 'C': 1},
         'B': {'S': 10},
         'C': {'S': 1},
         'D': {'E': 5},
         'E': {'D': 5, 'F': 7},
         'F': {'E': 7}}

@pytest.mark.parametrize("graph, start, dist", [
    (single_node_graph, 'S', {'S': 0}),
    (connected_graph, 'S', {'S': 0, 'B': 3, 'C': 1, 'D': 4, 'E': 2, 'F': 1, 'T': 4}),
    (connected_graph, 'F', {'S': 1, 'B': 2, 'C': 1, 'D': 3, 'E': 1, 'F': 0, 'T': 3}),
    (disconnected_graph, 'S', {'S': 0, 'B': 10, 'C': 1, 'D': math.inf, 'E': math.inf, 'F': math.inf}),
    (disconnected_graph, 'F', {'S': math.inf, 'B': math.inf, 'C': math.inf, 'D': 12, 'E': 7, 'F': 0})])
def test_breadth_first_search_no_end(graph, start, dist):
    assert Dijkstra().execute({"graph": graph, "start": start}) == dist

@pytest.mark.parametrize("graph, start, end, dist, path", [
    (single_node_graph, 'S', 'S', -1, None),
    (connected_graph, 'S', 'T', 4, ['S', 'F', 'E', 'B', 'T']),
    (connected_graph, 'F', 'T', 3, ['F', 'E', 'B', 'T']),
    (disconnected_graph, 'S', 'F', -1, None),
    (disconnected_graph, 'F', 'D', 12, ['F', 'E', 'D'])])
def test_breadth_first_search_no_end(graph, start, end, dist, path):
    assert Dijkstra().execute({"graph": graph, "start": start, "end": end}) == (dist, path)
# @pytest.mark.parametrize("graph, start, end, path", [
#     (single_node_graph, 'S', 'S', None),
#     (connected_graph, 'S', 'B', ['S', 'B'},
#     (connected_graph, 'S', 'T', ['S', 'B', 'T'},
#     (disconnected_graph, 'S', 'F', None),
#     (disconnected_graph, 'S', 'B', ['S', 'B'},}
# def test_breadth_first_search_with_end(graph, start, end, path):
#     assert BreadthFirstSearch().execute({"graph": graph, "start": start, "end": end}) == path
