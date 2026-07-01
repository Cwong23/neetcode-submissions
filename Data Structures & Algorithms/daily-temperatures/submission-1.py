class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # naive approach
        # start with first number and iterate until you find larger number and store # of iterations
        # repeat with next number and so on

        # last number must be 0 b/c there is no next number
        # the 2nd to last number depends on the last number
        # stack problem? backwardness of the list
        # 10 5 100
        # we store the position of where the next warmer temp is
        # [0, 1, 0]
        l = len(temperatures)
        result = [0 for i in range(l)]

        for i in range(l - 1, -1, -1):
            pos = i + 1

            while pos < l:
                if temperatures[pos] > temperatures[i]:
                    result[i] = pos - i
                    break
                elif result[pos] == 0:
                    break
                else:
                    pos += result[pos]
        return result