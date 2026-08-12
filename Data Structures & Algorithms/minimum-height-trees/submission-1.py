class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [0]
        graph = {}
        for edge in edges:
            x, y = edge[0], edge[1]
            if x not in graph:
                graph[x] = []
            if y not in graph:
                graph[y] = []
            graph[x].append(y)
            graph[y].append(x)
        
        visited = set()
        def dfs_height(curr: int) -> int:
            path = 0
            if curr in visited:
                return 0
            visited.add(curr)
            for x in graph[curr]:
                if x in visited:
                    continue
                path = max(dfs_height(x) + 1, path)
            return path

        heights = []
        min_path = float('inf')

        for key in graph.keys():
            curr_height = dfs_height(key)
            min_path = min(curr_height, min_path)
            heights.append((curr_height, key))
            visited = set()

        res = [x[1] for x in heights if x[0] == min_path]
        return res
