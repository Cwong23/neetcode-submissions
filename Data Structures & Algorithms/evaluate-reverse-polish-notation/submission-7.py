class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t.isdigit() or t[1:].isdigit():
                stack.append(int(t))
            else:
                num1, num2 = stack.pop(), stack.pop()
                match t:
                    case "+":
                        stack.append(num1 + num2)
                    case "-":
                        stack.append(num2 - num1)
                    case "*":
                        stack.append(num1 * num2)
                    case _:
                        stack.append(int(num2 / num1))
        return stack[0]