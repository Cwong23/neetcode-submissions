class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost)

        first, second = cost[0], cost[1]

        curr = 0
        for i in range(2, n):
            curr = min(first, second)+cost[i]
            first = second
            second = curr
        return min(first, second)
