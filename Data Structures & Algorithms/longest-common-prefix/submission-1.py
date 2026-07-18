class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        i = 0
        while True:
            if i >= len(strs[0]):
                break
            c = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != c:
                    break
            else:
                prefix+=c
                i+=1
                continue
            break

        return prefix