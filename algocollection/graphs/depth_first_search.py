from typing import Any, Mapping
from algocollection.common import Algorithm


class DepthFirstSearch(Algorithm):
    """Traverse all verticies connected to the starting vertex
    Depth First Search
    -------
    execute(self, param_dict: Mapping[str, Any]) -> Any:
        first, unpacks param_dict into graph and start (and maybe end)
        If end has not been passed in, returns a set of connected nodes
        Otherwise, return a path from the start to end node


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
        visited = set()
        visitor = {}
        stack = [start]
        while stack:
            vertex = stack.pop()
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    visitor[neighbour] = vertex
                    stack.append(neighbour)
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
