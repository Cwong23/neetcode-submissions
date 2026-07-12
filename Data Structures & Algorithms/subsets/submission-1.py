class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        def helper(subsets, curr, i):
            # keep
            if i >= len(nums):
                return
            
            curr.append(nums[i])
            subsets.append(curr[:])
            helper(subsets, curr, i+1)

            # don't keep
            curr.pop()
            helper(subsets, curr, i+1)

        helper(subsets, [], 0)
        return subsets