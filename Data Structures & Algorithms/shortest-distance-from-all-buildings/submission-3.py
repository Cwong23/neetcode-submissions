from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = [[0] * m for _ in range(n)]
        reach_count = [[0] * m for _ in range(n)]
        
        houses = set()
        obstacles = set()
        coords = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        # search for houses
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    houses.add((i,j))
                elif grid[i][j] == 2:
                    obstacles.add((i,j))

        total_houses = len(houses)
        
        # bfs for all possible houses
        for house in houses:
            visited = obstacles.copy()
            queue = deque([[house[0], house[1], 0]])
            while queue:
                i, j, dist = queue.popleft()
                if (i, j) in visited:
                    continue
                visited.add((i, j))

                if (i, j) not in houses and (i, j) not in obstacles:
                    res[i][j] += dist
                    reach_count[i][j] += 1

                for coord in coords:
                    i_new, j_new = i + coord[0], j + coord[1]
                    if i_new >= 0 and i_new < n and j_new >= 0 and j_new < m and (grid[i_new][j_new] != 1 and grid[i_new][j_new] != 2):
                        queue.append([i_new, j_new, dist+1])
        
        ans = float('inf')
        for i in range(n):
            for j in range(m):
                if (i,j) not in obstacles and (i,j) not in houses:
                    if reach_count[i][j] == total_houses:
                        ans = min(ans, res[i][j])
        return -1 if ans == float('inf') else ans
            
        