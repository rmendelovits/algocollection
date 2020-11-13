"""Unit tests for greatest common divisor."""

from algocollection.graphs import Prim

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

@pytest.mark.parametrize("graph, start, edge_set", [
    (single_node_graph, 'S', set()),
    (connected_graph, 'S', {('C', 'S'), ('C', 'F'), ('B', 'E'), ('E', 'F'), ('B', 'T'), ('B', 'D')}),
    (connected_graph, 'F', {('C', 'S'), ('C', 'F'), ('B', 'E'), ('E', 'F'), ('B', 'T'), ('B', 'D')}),
    (disconnected_graph, 'S', {('B', 'S'), ('C', 'S')}),
    (disconnected_graph, 'F', {('D', 'E'), ('E', 'F')})])
def test_prim(graph, start, edge_set):
    assert Prim().execute({"graph": graph, "start": start}) == edge_set
