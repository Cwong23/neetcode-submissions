class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums)//2
        cache = {}
        def backtrack(i, curr):
            if i >= len(nums):
                return curr == target
            
            if (i, curr) in cache:
                return cache[(i, curr)]
            if backtrack(i+1, curr+nums[i]):
                cache[(i, curr)] = True
                return True
            
            if backtrack(i+1, curr):
                cache[(i, curr)] = True
                return True
            cache[(i, curr)] = False
            return False
        
        return backtrack(0, 0)
