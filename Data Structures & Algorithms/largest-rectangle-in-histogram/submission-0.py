class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = heights[0]
        mon_stack = []

        for i, h in enumerate(heights):
            start = i
            while mon_stack and mon_stack[-1][-1] > h:
                idx, height = mon_stack.pop()
                res = max(res, height*(i-idx))
                start = idx
            mon_stack.append((start, h))
        
        for i, h in mon_stack:
            res = max(res, h*(len(heights)-i))

        return res

