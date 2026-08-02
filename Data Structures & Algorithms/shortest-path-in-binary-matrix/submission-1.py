class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # graph
        # finding shortest path from top left to bottom right
        # n by m grid
        # contains 0's and 1's where 0's are areas we can go and 1's are not
        # returning the longest path length or -1 if there is none
        
        # BFS 
        # by searching layer by layer, we can guarentee that we will find the shortest path
        # for loop + queue
        # items in queue
            # coords and path length?
            # is it possible that by searching one area, it can result in a larger path length?
        res = -1
        queue = []

        if grid[0][0] == 1:
            return res
        # (i, j, path_len)
        N = len(grid)


        queue.append((0, 0 , 1))
        grid[0][0] = 1

        dirs = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1), (0, 1),
                (1, -1), (1, 0), (1, 1)]
        check = 1
        while queue:
            current_positions = check
            check = 0
            for i in range(current_positions):
                curr = queue.pop(0)
                y, x, path_len = curr
                if (y, x) == (N - 1, N - 1):
                    return path_len
                for d in dirs:
                    temp_x, temp_y = x + d[1], y + d[0]
                    if 0 <= temp_x < N and 0 <= temp_y < N:
                        if grid[temp_y][temp_x] == 0:
                            grid[temp_y][temp_x] = 1
                            check+=1
                            queue.append((temp_y, temp_x, path_len+1))
        return res











