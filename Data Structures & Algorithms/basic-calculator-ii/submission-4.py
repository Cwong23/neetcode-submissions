class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr = 0
        s = s.replace(" ", "")
        op = "+"
        
        for i, ch in enumerate(s):
            if ch.isdigit():
                curr = 10 * curr + int(ch)
            if (not ch.isdigit() or i == len(s) - 1):
                if op == "+":
                    stack.append(curr)
                elif op == "-":
                    stack.append(-curr)
                elif op == "*":
                    stack.append(stack.pop() * curr)
                else:
                    prev = stack.pop()
                    stack.append(int(prev / curr))
                op = ch
                curr = 0

        return sum(stack)