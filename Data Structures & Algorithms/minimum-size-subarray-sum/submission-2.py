class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        n = len(nums)
        if sum(nums) == target:
            return n
        
        res = n
        l = 0
        window = 0

        for r, num in enumerate(nums):
            window+=num
            while window >= target:
                res = min(res, r - l + 1)
                window-=nums[l]
                l+=1
        
        return res