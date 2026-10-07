class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        options = set(nums)
        n_len = len(nums)

        def backtrack(size):
            nonlocal n_len
            if n_len == size:
                res.append(curr[:])
                return

            for n in nums:
                if n in options:
                    options.remove(n)
                    curr.append(n)
                    backtrack(size+1)
                    curr.pop()
                    options.add(n)

        backtrack(0)
        return res