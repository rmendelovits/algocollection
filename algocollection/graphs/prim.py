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

from algocollection.common import Algorithm, DLogTime, DTime, GraphTime


class Prim(Algorithm):
    """Generate a minimum weight spanning tree from a graph and a start node
    Prim's algorithm
    -------
    execute(self, param_dict) -> Any:
        first, unpacks param_dict into graph and start
        then finds a minimum spanning tree
        from start to all connected vertecies


    Notes
    -----
    Time Complexity:
        Let |V| be the number of verticies
        Let |E| be the number of edges
        T(n) = O(|E| log |V|)
    """
    def execute(self, param_dict) -> Any:
        # unpack the param_dict
        if ('graph' not in param_dict or 'start' not in param_dict):
            raise ValueError("Prim requires" +
                             "a graph and a starting vertex")
        graph = param_dict['graph']
        start = param_dict['start']

        # actual algorthm
        mst_missing_verticies = set()
        priority_queue = []
        edge_set = set()
        for vertex in graph:
            mst_missing_verticies.add(vertex)
        mst_missing_verticies.remove(start)
        for neighbour in graph[start]:
            if start < neighbour:
                heapq.heappush(priority_queue, (graph[start][neighbour],
                                                (start, neighbour)))
            else:
                heapq.heappush(priority_queue, (graph[start][neighbour],
                                                (neighbour, start)))
        while mst_missing_verticies and priority_queue:
            min_edge = heapq.heappop(priority_queue)[1]
            new_vertex = None
            # note: only one of these can be true
            #     because one of the two ends is in the tree already
            if min_edge[0] in mst_missing_verticies:
                new_vertex = min_edge[0]
            elif min_edge[1] in mst_missing_verticies:
                new_vertex = min_edge[1]
            if new_vertex is not None:
                edge_set.add(min_edge)
                mst_missing_verticies.remove(new_vertex)
                for neighbour in graph[new_vertex]:
                    if new_vertex < neighbour:
                        heapq.heappush(priority_queue,
                                       (graph[new_vertex][neighbour],
                                        (new_vertex, neighbour)))
                    else:
                        heapq.heappush(priority_queue,
                                       (graph[new_vertex][neighbour],
                                        (neighbour, new_vertex)))
        return edge_set

    def best_case_time_complexity(self):
        return (DLogTime.constant, DLogTime.constant)

    def average_case_time_complexity(self):
        return GraphTime.elogv

    def worst_case_time_complexity(self):
        return GraphTime.elogv

    def worst_case_space_complexity(self):
        return (DTime.linear, DLogTime.linear)
