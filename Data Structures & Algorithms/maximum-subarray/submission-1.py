class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # back tracking? brute force
            # finding all sub arrays
            # o(n * 2^n)
            # either keep or number or don't

        
        # dp?
        # at each point, store the max value of the sub array
        # compare that to the current to determine what the current max value is

        dp = nums[:]
        
        for i in range(1, len(dp)):
            dp[i] = max(dp[i], dp[i-1] + dp[i])

        return max(dp)