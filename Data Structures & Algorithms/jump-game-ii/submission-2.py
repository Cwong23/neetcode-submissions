class Solution:
    def jump(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        if n == 1:
            return 0
        res = 1
        while i <= n:
            if (i + nums[i]) >= n - 1:
                break
            jump = 0
            max_idx = 0
            for j in range(1, min(nums[i] + 1, n)):
                if jump < (nums[i + j] + j):
                    jump = nums[i + j] + j
                    max_idx = j
            res += 1
            i += max_idx
        return res