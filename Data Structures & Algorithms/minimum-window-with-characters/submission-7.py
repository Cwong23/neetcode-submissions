class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        count = len(t)
        window = {}
        for c in t:
            window[c] = window.get(c, 0) + 1

        left = 0
        res = ""
        for right, c in enumerate(s):
            if c in window:
                window[c]-=1
                if window[c] > -1:
                    count-=1
            if count == 0:
                if len(res) > len(s[left:right+1]) or res == "":
                    res = s[left:right+1]
            while count == 0:
                if s[left] in window:
                    window[s[left]]+=1
                    if window[s[left]] > 0:
                        count+=1
                if count == 1:
                    if len(res) > len(s[left:right+1]) or res == "":
                        res = s[left:right+1]
                left+=1
        return res