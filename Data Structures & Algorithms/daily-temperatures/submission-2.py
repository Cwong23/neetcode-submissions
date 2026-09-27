class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res, stack = [0], [(temperatures[-1], n-1)]

        for i in range(n - 2, -1, -1):
            curr = temperatures[i]
            while stack:
                if curr < stack[-1][0]:
                    # found larger temp
                    res.append(stack[-1][1] - i)
                    stack.append((curr, i))
                    break
                else:
                    # need to keep popping
                    stack.pop()
            else:
                res.append(0)
                stack.append((curr, i))

        return res[::-1]