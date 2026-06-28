class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = {'[': ']', '(': ')', '{': '}'}



        for c in s:
            if c in opens:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                x = stack.pop()
                if opens[x] != c:
                    return False
        if len(stack) != 0:
            return False
        return True