class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        if len(nums) <= 2:
            return max(nums)
        
        dp[-1], dp[-2] = nums[-1], nums[-2]

        for i in range(len(nums) - 3, -1, -1):
            dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])

        print(dp)
        return max(dp[0], dp[1])