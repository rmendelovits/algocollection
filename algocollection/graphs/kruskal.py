""" algocollection - find minimum weight spanning tree
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

import heapq
from typing import Any, Mapping

from algocollection.common import Algorithm, DLogTime, DTime


class Kruskal(Algorithm):
    """Generate a minimum weight spanning forest from a graph
    Kruskal's Algorithm
    -------
    execute(self, param_dict: Mapping[str, Any]) -> Any:
        first, unpacks param_dict into graph and start
        then finds a minimum spanning forest


    Notes
    -----
    Time Complexity:
        Let |V| be the number of verticies
        Let |E| be the number of edges
        T(n) = O(|E| log |V|)
    """
    def execute(self, param_dict: Mapping[str, Any]) -> Any:
        # unpack the param_dict
        if ('graph' not in param_dict):
            raise ValueError("Kruskal requires a graph")
        graph = param_dict['graph']

        # actual algorthm
        connected_verticies = []
        priority_queue = []
        edge_set = set()
        for vertex in graph:
            connected_verticies.append({vertex})
            for neighbour in graph[vertex]:
                heapq.heappush(priority_queue, (graph[vertex][neighbour],
                                                (vertex, neighbour)))
        while priority_queue:
            min_edge = heapq.heappop(priority_queue)[1]
            min_edge_sets = [tree for tree in connected_verticies
                             if min_edge[0] in tree
                             or min_edge[1] in tree]
            if len(min_edge_sets) == 2:
                edge_set.add(min_edge)
                connected_verticies.append(min_edge_sets[0] | min_edge_sets[1])
                connected_verticies.remove(min_edge_sets[0])
                connected_verticies.remove(min_edge_sets[1])
        return edge_set

    def best_case_time_complexity(self):
        return (DLogTime.constant, DLogTime.constant)

    def average_case_time_complexity(self):
        return (DLogTime.constant, DTime.linearithmic)

    def worst_case_time_complexity(self):
        return (DLogTime.constant, DTime.linearithmic)

    def worst_case_space_complexity(self):
        return (DTime.linear, DLogTime.linear)
