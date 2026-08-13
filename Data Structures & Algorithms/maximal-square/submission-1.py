class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        res = 0
        for i in range(m):
            if matrix[0][i] == "1":
                dp[0][i] = 1
                res = 1
        for i in range(n):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                res = 1

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == "1":
                    dp[i][j] = 1
                    if dp[i-1][j] != 0 and dp[i][j-1] != 0:
                        dp[i][j]+=dp[i-1][j-1]
                    res = max(dp[i][j], res)
        print(dp)
        return res*res