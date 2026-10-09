class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            s, t = t, s
        
        if len(t) - len(s) > 1:
            return False

        if len(s) == len(t):
            return sum(a != b for a, b in zip(s, t)) == 1
        
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                return s[i:] == t[j+1:]
        return True