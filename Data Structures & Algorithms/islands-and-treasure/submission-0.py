from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        coords = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        queue = deque()
        N, M = len(grid), len(grid[0])
        
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0:
                    queue.append([i, j])
        
        while queue:
            i, j = queue.popleft()
            dist = grid[i][j]
            for coord in coords:
                # check areas around it
                new_i, new_j = i + coord[0], j + coord[1]
                if (new_i < 0 or new_i >= N 
                    or new_j < 0 or new_j >= M 
                    or grid[new_i][new_j] != 2147483647):
                    continue
                grid[new_i][new_j] = dist+1
                queue.append([new_i, new_j])
        return
