class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        nums_to_letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        sol = []
        len_digits = len(digits)
        def dfs(i: int, curr: str):
            if i == len_digits:
                sol.append(curr)
                return
            chars = nums_to_letters[int(digits[i])]
            for c in chars:
                dfs(i+1, curr+c)
            return

        dfs(0, "")

        return sol