from typing import Any, Mapping
from algocollection.common import Algorithm, DLogTime, DTime
import heapq


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
        connected_verticies = set()
        priority_queue = []
        edge_set = set()
        for vertex in graph:
            connected_verticies.add(tuple(vertex))
            for neighbour in graph[vertex]:
                heapq.heappush(priority_queue, (graph[vertex][neighbour], (vertex, neighbour)))
        while priority_queue:
            min_edge = heapq.heappop(priority_queue)[1]
            min_edge_sets = [tree for tree in connected_verticies if min_edge[0] in tree or min_edge[1] in tree]
            if len(min_edge_sets) == 2:
                edge_set.add(min_edge)
                connected_verticies.add(tuple(set(min_edge_sets[0] + min_edge_sets[1])))
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
