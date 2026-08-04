class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        dp = [[(0, False)] * len(nums) for _ in range(len(nums))]

        for i in range(len(nums)):
            dp[0][i] = (1, True)

        for i in range(1, len(nums)):
            for j in range(i, len(nums)):
                diag = dp[i-1][j-1]
                above = dp[i-1][j]
                if i-2<0:
                    diag_above = 0
                else:    
                    diag_above = dp[i-2][j - 1][0]

                temp = diag[0] + above[0] - diag_above
                x = False
                if diag[1] and nums[j-1] < nums[j]:
                    x = True
                    temp+=1
                dp[i][j] = (temp, x)

        return dp[-1][-1][0]