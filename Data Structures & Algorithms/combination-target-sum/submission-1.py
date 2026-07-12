class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(subset, s, i):
            if s == target:
                res.append(subset[:])
                return

            if s > target or i>=len(nums):
                return
            
            # include curr
            subset.append(nums[i])
            backtrack(subset, s + nums[i], i)
            subset.pop()

            # do not include either
            backtrack(subset, s, i+1)
            return

        backtrack([], 0, 0)
        return res