class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [amount+1] * (amount + 1) # O(m) space where m is amount
        coins.sort() # O(n log n)

        if coins[0] > amount:
            return -1
        
        for c in coins:
            if c < len(dp):
                dp[c] = 1

        for i in range(1, len(dp)):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i-c] + 1, dp[i])
        print(dp)
        return dp[amount] if dp[amount] != amount + 1 else -1

        