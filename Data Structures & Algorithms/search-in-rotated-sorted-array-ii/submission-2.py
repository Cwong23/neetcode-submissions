class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left<=right:
            middle = left + (right-left) // 2
            val = nums[middle]
            if val == target:
                return True

            if nums[left] == val == nums[right]:
                left+=1
                right-=1
            elif nums[left] <= val:
                if nums[left] <= target < val:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if val < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return False
                    