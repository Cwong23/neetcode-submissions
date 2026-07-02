class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        if n <= 2:
            return max(nums)
        
        dp[-1], dp[-2] = nums[-1], nums[-2]

        for i in range(n - 3, -1, -1):
            dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])

        return dp[0]