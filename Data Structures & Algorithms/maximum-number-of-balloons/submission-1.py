class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {}
        for c in text:
            d[c] = d.get(c, 0) + 1
        
        res = 0
        while True:
            for c in "balloon":
                if c not in d or d[c] == 0:
                    break
                d[c]-=1
            else:
                res+=1
                continue
            break
        
        return res