class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for i in range(len(s))]
        res_i = 0
        res_len = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(s) - 1, -1, -1):
                if s[i] == s[j] and (j - i <=2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j - i + 1 > res_len:
                        res_i = i
                        res_len = j - i + 1

        return s[res_i:res_len + res_i] 
