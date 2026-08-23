class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        stack = []
        n = len(s)
        cache = {}

        def is_pal(s):
            if s in cache:
                return cache[s]
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    cache[s] = False
                    return False
                i+=1
                j-=1
            cache[s] = True
            return True

        def backtrack(i):
            if i == n:
                res.append(stack[:])
                return
            
            for j in range(i+1, n+1):
                if is_pal(s[i:j]):
                    stack.append(s[i:j])
                    backtrack(j)
                    stack.pop()
            return
        backtrack(0)

        return res