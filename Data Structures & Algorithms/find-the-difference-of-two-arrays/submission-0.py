class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        res1, res2 = set1 - set2, set2 - set1
        return [list(res1), list(res2)]