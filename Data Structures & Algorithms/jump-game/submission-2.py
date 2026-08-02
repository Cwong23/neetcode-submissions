class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True

        for i in range(len(nums)):
            if dp[i]:
                for x in range(nums[i]):
                    if i+x+1 < len(nums):
                        dp[i+x+1] = True
        return dp[-1]