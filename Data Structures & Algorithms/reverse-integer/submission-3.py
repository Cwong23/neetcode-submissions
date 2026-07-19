class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x*=-1
        
        res = 0
        while x >= 1:
            t = x
            temp = t % 10
            res *= 10
            res = int(res+temp)
            x = int(x) / 10
            if res < -2**31 or res > 2**31 - 1:
                return 0
        
        return int(res * -1) if negative else int(res)