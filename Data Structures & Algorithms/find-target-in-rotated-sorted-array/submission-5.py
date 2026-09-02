class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r + 1:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                # normal
                if nums[mid] < target or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # rotated
                if nums[mid] > target or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1