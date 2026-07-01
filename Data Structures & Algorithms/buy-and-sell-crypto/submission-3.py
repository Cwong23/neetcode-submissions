class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            max_profit = max(max_profit, prices[right] - prices[left])
            if prices[left] > prices[right]:
                left=right
            right+=1
        # while left < len(prices) - 1:
        #     max_profit = max(max_profit, prices[right - 1] - prices[left])
        #     left+=1
        return max_profit