class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.reverse()
        dp = [0] * len(nums)
        if len(nums) <= 2:
            return max(nums)
        
        dp[0], dp[1] = nums[0], nums[1]

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        print(dp)
        return max(dp[-1], dp[-2])