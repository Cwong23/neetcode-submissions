class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+",
            "-",
            "*",
            "/",
        }

        stack = []
        i = 0

        while i < len(tokens):
            print(stack)
            if tokens[i] in operations:
                b = stack.pop()
                a = stack.pop()
                match tokens[i]:
                    case "+":
                        stack.append(a + b)
                    case "-":
                        stack.append(a - b)
                    case "*":
                        stack.append(a * b)
                    case "/":
                        stack.append(int(a / b))
            else:
                stack.append(int(tokens[i]))
            i+=1
        return int(stack[0])


        # treat tokens like stack
        # figure out operation, pop
        # get number, pop
        # get operation
        # repeat
        # if two numbers in a row, then stop because that's the bottom