class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        dp1 = [0] * (n-1)
        nums1 = nums[1:]
        dp1[0] = nums1[0]
        dp1[1] = max(nums1[0], nums1[1])

        dp2 = [0] * (n-1)
        nums2 = nums[:-1]
        dp2[0] = nums2[0]
        dp2[1] = max(nums2[0], nums2[1])

        for i in range(2, n-1):
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums1[i])
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums2[i])
        return max(dp1[-1], dp2[-1])

"""

Houses are arranged in circle
Get max money out
Can't rob two adjacent houses

Thought:
    Go backwards b/c -1 would end up at end of list

State: House in nums
Means: Max amount of money at given point
Needs: Max amount of money if rob current and max amount of money if skip
Decides: take the max of either since all possibles values will be calculated
Combines: take max money and either add or not add


"""

        