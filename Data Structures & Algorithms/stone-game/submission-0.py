class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # each person should take the largest of the front or the back at a time
        res = 0

        # what is the optimal move?

        # 1 2 3 1
        # need to also compare what the 2nd largest number is?
        # 2 3 1
        # need to calculate all possible combinations
        # how do we go about calculating that?
        # backtracking?
        # either take the first or last element
        # where do we start?
        # need 2 different DP's?
            # reference eachother
        dp_first = []
        dp_last = []









        for x in piles:
            res = 1 - res

        return res == 0