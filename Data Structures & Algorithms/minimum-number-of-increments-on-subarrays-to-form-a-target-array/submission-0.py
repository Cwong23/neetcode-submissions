class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        operations = target[0] + sum(max(0, target[i] - target[i-1]) for i in range(1, n))
        return operations










