class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        n = len(nums)
        nums.sort()
        dups = set()

        def dfs(i, curr):
            if i >= n:
                return
            curr.append(nums[i])
            if tuple(curr[:]) not in dups:
                res.append(curr[:])
                dups.add(tuple(curr[:]))

            for j in range(i+1, n):
                dfs(j, curr)
            curr.pop()
            dfs(i+1, [])

        dfs(0, [])
        return res