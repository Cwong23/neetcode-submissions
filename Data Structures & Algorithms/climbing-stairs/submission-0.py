class Solution:
    def climbStairs(self, n: int) -> int:
        # dp problem
        # 1D
        # have array that is len n
        # start from i = 0
        # that will be 1
        # also fill in i = 1 to be 2
        # start with i = 2 for loop
        # reference the previous step and the prev prev step and add those
        # [ 1, 2, 3, 5]

        dp = [1 , 2]
        if n < 3:
            return dp[n - 1]

        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[-1]