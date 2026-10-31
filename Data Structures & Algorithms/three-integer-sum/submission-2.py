class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()

        for i, target in enumerate(nums[:n-2]):
            ptr1, ptr2 = i + 1, n - 1
            while ptr1 < ptr2:
                if nums[ptr1] + nums[ptr2] + target == 0:
                    res.add(tuple([target, nums[ptr1], nums[ptr2]]))
                    ptr1+=1
                    ptr2-=1
                elif nums[ptr1] + nums[ptr2] + target > 0:
                    ptr2 -= 1
                else:
                    ptr1 += 1

        return [list(x) for x in res]