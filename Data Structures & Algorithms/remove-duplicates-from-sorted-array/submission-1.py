class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = len(nums) - 2
        while i >= 0:
            if nums[i] == nums[i+1]:
                del nums[i+1]
            i-=1
        return len(nums)