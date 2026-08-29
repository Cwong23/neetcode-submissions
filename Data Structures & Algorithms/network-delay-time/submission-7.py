import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set([i for i in range(1, n+1)])
        graph = {}

        for f, t, time in times:
            if f not in graph:
                graph[f] = []
            graph[f].append([t, time])
        
        heap = [[0, k]]
        last_node = k
        nodes = {}
        while heap:
            curr = heapq.heappop(heap)
            if curr[1] not in visited:
                continue
            last_node = curr[1]
            visited.remove(curr[1])
            nodes[last_node] = curr[0]
            if curr[1] in graph:
                for node in graph[curr[1]]:
                    temp = node[1] + curr[0]
                    heapq.heappush(heap, [temp, node[0]])
        return nodes[last_node] if len(visited) == 0 else -1