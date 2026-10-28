import re

class Solution:
    def expand(self, s: str) -> List[str]:
        # dfs + string parsing
        # 

        res = []
        all_c = []
        choices = []
        curr = []

        flag = False
        for c in s:
            if c == ",":
                continue
            if c == "{":
                flag = True
                curr = []
                all_c.append(str(len(choices)))
                continue
            elif c == "}":
                flag = False
                choices.append(curr[:])
                continue
            
            if flag:
                curr.append(c)
            else:
                all_c.append(c)

        def dfs(curr, ptr):
            if len(curr) == len(all_c):
                res.append(curr)
                return
            
            if all_c[ptr].isdigit():
                for c in choices[int(all_c[ptr])]:
                    dfs(curr+c, ptr+1)
            else:
                dfs(curr+all_c[ptr], ptr+1)
        dfs("", 0)

        return res