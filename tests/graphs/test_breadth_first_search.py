"""Unit tests for greatest common divisor."""

import pytest
from algocollection.graphs import BreadthFirstSearch

single_node_graph = {'S': set()}

connected_graph = {'S': set(['B', 'C', 'F']),
                   'B': set(['S', 'D', 'E', 'T']),
                   'C': set(['S', 'F']),
                   'D': set(['B']),
                   'E': set(['B', 'F']),
                   'F': set(['S', 'C', 'E']),
                   'T': set(['B'])}

disconnected_graph = {'S': set(['B', 'C']),
                      'B': set(['S']),
                      'C': set(['S']),
                      'D': set(['E']),
                      'E': set(['D', 'F']),
                      'F': set(['E'])}


@pytest.mark.parametrize("graph, start, connected_verticies", [
    (single_node_graph, 'S', set(['S'])),
    (connected_graph, 'S', set(['S', 'B', 'C', 'D', 'E', 'F', 'T'])),
    (connected_graph, 'F', set(['S', 'B', 'C', 'D', 'E', 'F', 'T'])),
    (disconnected_graph, 'S', set(['S', 'B', 'C'])),
    (disconnected_graph, 'F', set(['D', 'E', 'F']))])
def test_breadth_first_search_no_end(graph, start, connected_verticies):
    assert BreadthFirstSearch().execute({"graph": graph,
                                         "start": start}) == connected_verticies


@pytest.mark.parametrize("graph, start, end, path", [
    (single_node_graph, 'S', 'S', None),
    (connected_graph, 'S', 'B', ['S', 'B']),
    (connected_graph, 'S', 'T', ['S', 'B', 'T']),
    (disconnected_graph, 'S', 'F', None),
    (disconnected_graph, 'S', 'B', ['S', 'B'])])
def test_breadth_first_search_with_end(graph, start, end, path):
    assert BreadthFirstSearch().execute({"graph": graph,
                                         "start": start,
                                         "end": end}) == path
