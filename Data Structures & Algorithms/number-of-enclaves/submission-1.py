class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        stack = []
        for i in range(len(grid)):
            if grid[i][0] == 1:
                stack.append((i, 0))
                grid[i][0] = 0
            if grid[i][-1] == 1:
                stack.append((i, len(grid)-1))
                grid[i][-1] = 0

        for i in range(len(grid[0])):
            if grid[0][i] == 1:
                stack.append((0, i))
                grid[0][i] = 0
            if grid[-1][i] == 1:
                stack.append((len(grid[0])-1, i))
                grid[-1][i] = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while stack:
            i, j = stack.pop()
            for d in directions:
                x, y = d
                if i+x >= 0 and i+x < len(grid) and j+y >=0 and j+y < len(grid[0]):
                    if grid[i+x][j+y] == 1:
                        grid[i+x][j+y] = 0
                        stack.append((i+x, j+y))

        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res+=grid[i][j]

        return res