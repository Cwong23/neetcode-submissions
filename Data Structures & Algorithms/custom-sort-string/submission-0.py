class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        
        res = ""
        i = 0
        while i < len(order):
            if order[i] not in d:
                i+=1
            else:
                if d[order[i]] == 0:
                    i+=1
                else:
                    res+=order[i]
                    d[order[i]]-=1
        i = 0
        while i < len(s):
            if d[s[i]] == 0:
                i+=1
            else:
                res+=s[i]
                d[s[i]]-=1
        return res
