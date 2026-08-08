class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = [0] * (n + 1)
        res = l = cnt = 0
    
        for r in range(n):
            count[nums[r]] += 1
            if count[nums[r]] == 1:
                k-=1
            if k < 0:
                count[nums[l]]-=1
                l+=1
                k+=1
                cnt=0
            if k == 0:
                while count[nums[l]] > 1:
                    count[nums[l]] -= 1
                    l += 1
                    cnt += 1
                res += (cnt + 1)
        return res