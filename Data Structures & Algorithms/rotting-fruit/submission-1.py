from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid[0]), len(grid)
        queue = deque()
        fruits = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append([i, j])
                elif grid[i][j] == 1:
                    fruits.add((i, j))

        if not fruits:
            return 0

        res = -1
        while queue:
            moves = len(queue)
            for i in range(moves):
                curr = queue.popleft()
                for d in directions:
                    y, x = curr[0] + d[0], curr[1] + d[1]
                    if y < 0 or y >= n or x < 0 or x >= m or grid[y][x] != 1:
                        continue
                    fruits.remove((y, x))
                    grid[y][x] = 2
                    queue.append([y, x])
            res+=1
        if fruits:
            return -1
        return res