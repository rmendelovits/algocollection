from typing import Any, Mapping
from algocollection.common import Algorithm, DLogTime, DTime


class BreadthFirstSearch(Algorithm):
    """Traverse all verticies connected to the starting vertex
    Breadth First Search
    -------
    execute(self, param_dict: Mapping[str, Any]) -> Any:
        first, unpacks param_dict into graph and start (and maybe end)
        If end has not been passed in, returns a set of connected nodes
        Otherwise, return a shortest path between start and end


    Notes
    -----
    Time Complexity:
        Let |V| be the number of verticies
        Let |E| be the number of edges
        T(n) = O(|V| + |E|)
    """
    def execute(self, param_dict: Mapping[str, Any]) -> Any:
        # unpack the param_dict
        if ('graph' not in param_dict or 'start' not in param_dict):
            raise ValueError("BreadthFirstSearch requires a graph and a starting vertex")
        graph = param_dict['graph']
        start = param_dict['start']
        if 'end' in param_dict:
            end = param_dict['end']

        # actual algorthm
        visited = set([start])
        visitor = {}
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    visitor[neighbour] = vertex
                    queue.append(neighbour)
        if 'end' in param_dict:
            if end not in visitor:
                return None
            path = []
            current_vertex = end
            while current_vertex != start:
                path.insert(0, current_vertex)
                current_vertex = visitor[current_vertex]
            path.insert(0, start)
            return path
        return visited

    def best_case_time_complexity(self):
        return (DTime.linear, DTime.linear)

    def average_case_time_complexity(self):
        return (DTime.linear, DTime.linear)

    def worst_case_time_complexity(self):
        return (DTime.linear, DTime.linear)

    def worst_case_space_complexity(self):
        return (DTime.linear, DLogTime.constant)
