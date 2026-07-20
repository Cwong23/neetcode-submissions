class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtracking
        # either include or not include number
        # all integers are unqiue within nums
        # o(n!)
        res = []
        curr_values = set()

        def backtrack(combo):
            if len(combo) == len(nums):
                res.append(combo[:])
                return
            for x in nums:
                if x not in curr_values:
                    curr_values.add(x)
                    combo.append(x)
                    backtrack(combo)
                    combo.pop()
                    curr_values.remove(x)
            return
        
        backtrack([])

        return res