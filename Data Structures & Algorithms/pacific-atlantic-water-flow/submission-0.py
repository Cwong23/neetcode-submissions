from collections import deque

class Solution:
    def pacificAtlantic(self, heights):
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(starts, visit):
            queue = deque(starts)
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS
                            and (nr, nc) not in visit
                            and heights[nr][nc] >= heights[r][c]):
                        visit.add((nr, nc))
                        queue.append((nr, nc))



        pac_starts  = [(0, c) for c in range(COLS)] + [(r, 0) for r in range(ROWS)]
        atl_starts  = [(ROWS - 1, c) for c in range(COLS)] + [(r, COLS - 1) for r in range(ROWS)]

        pacific = set(pac_starts)
        atlantic = set(atl_starts)

        bfs(pac_starts, pacific)
        bfs(atl_starts, atlantic)

        return [list(cell) for cell in pacific & atlantic]