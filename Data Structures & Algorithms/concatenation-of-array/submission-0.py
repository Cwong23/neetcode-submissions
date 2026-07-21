class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        while i < n:
            nums.append(nums[i])
            i+=1
        return nums