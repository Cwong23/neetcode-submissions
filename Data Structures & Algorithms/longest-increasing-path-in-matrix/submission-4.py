from collections import deque

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for _ in range(M)]

        def dfs(r, c):
            if dp[r][c]:
                return dp[r][c]
            best = 1
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < M and 0 <= nc < N and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))
            dp[r][c] = best
            return best

        res = 0
        for r in range(M):
            for c in range(N):
                res = max(res, dfs(r, c))
        return res
