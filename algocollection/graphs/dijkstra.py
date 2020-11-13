from typing import Any, Mapping
from algocollection.common import Algorithm, DLogTime, DTime
import math
import heapq

class Dijkstra(Algorithm):
    """Find the shortest distance from start to every vertex (or end)
    Dijkstra
    -------
    execute(self, param_dict: Mapping[str, Any]) -> Any:
        first, unpacks param_dict into graph and start (and maybe end)
        If end has not been passed in, returns the cost to every vertex
        Otherwise, return the cost and a shortest path between start and end


    Notes
    -----
    Time Complexity:
        Let |V| be the number of verticies
        Let |E| be the number of edges
        T(n) = O(|V| log |V| + |E|)
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
        dist = {start: 0}
        visitor = {}
        priority_queue = []
        for vertex in graph:
            if vertex != start:
                dist[vertex] = math.inf
            heapq.heappush(priority_queue, (dist[vertex], vertex))

        while priority_queue:
            vertex = heapq.heappop(priority_queue)[1]
            for neighbour in graph[vertex]:
                alt = dist[vertex] + graph[vertex][neighbour]
                if not math.isinf(dist[vertex]) and math.isinf(dist[neighbour]) or alt < dist[neighbour]:
                    neighbour_index = next((index for (index, d) in enumerate(priority_queue) if d[1] == neighbour))
                    priority_queue.remove(priority_queue[neighbour_index])
                    new_dist = alt
                    if not math.isinf(dist[neighbour]):
                        new_dist = priority_queue[neighbour_index][0] - alt
                    heapq.heappush(priority_queue, (new_dist, neighbour))
                    dist[neighbour] = alt
                    visitor[neighbour] = vertex

        if 'end' in param_dict:
            if end not in visitor:
                return -1, None
            path = []
            current_vertex = end
            while current_vertex != start:
                path.insert(0, current_vertex)
                current_vertex = visitor[current_vertex]
            path.insert(0, start)
            return dist[end], path
        return dist

    def best_case_time_complexity(self):
        return (DTime.linearithmic, DTime.linear)

    def average_case_time_complexity(self):
        return (DTime.linearithmic, DTime.linear)

    def worst_case_time_complexity(self):
        return (DTime.linearithmic, DTime.linear)

    def worst_case_space_complexity(self):
        return (DTime.linear, DLogTime.constant)
