class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) <= 2:
            return nums[0]

        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]

        while l <= r:
            mid = (r + l) // 2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            if mid % 2 == 0:
                if nums[mid] == nums[mid-1]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] == nums[mid-1]:
                    l = mid + 1
                else:
                    r = mid - 1


        return -1