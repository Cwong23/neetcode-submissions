class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        curr = []
        def backtrack(ptr, size):
            if size == k:
                res.append(curr[:])
                return
            
            for i in range(ptr, n+1):
                curr.append(i)
                backtrack(i+1, size+1)
                curr.pop()
            return
        backtrack(1, 0)
        return res