class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums) + 2)
        postfix = [0] * (len(nums) + 2)
        dp = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] == 1:
                prefix[i + 1] = prefix[i] + 1

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 1:
                postfix[i + 1] = postfix[i + 2] + 1

        for i in range(len(nums)):
            if nums[i] == 1:
                dp[i] = max(prefix[i], postfix[i + 1])
            else:
                dp[i] = prefix[i] + postfix[i + 2] + 1

        return max(dp)