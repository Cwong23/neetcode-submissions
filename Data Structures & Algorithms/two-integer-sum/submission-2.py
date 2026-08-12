class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store hash map {diff: idx}
        diffs: dict[int, int] = {}

        for j in range(len(nums)):
            key: int = nums[j]
            if key in diffs:
                return [diffs[key], j]
            diff = target - key
            diffs[diff] = j
