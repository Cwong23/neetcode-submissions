class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = -1
        while l < r:
            s = nums[l] + nums[r]
            if s < k:
                res = max(res, s)
            if s < k:
                l += 1
            else:
                r -= 1

        return res