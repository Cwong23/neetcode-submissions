class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # find the max area
        # calc area function?
        # always try to pick the highest bar
        # also try to maximize the distance b/c it means most water
        # start at max distance
        # two pointer one at start and one at end
        # move the pointer with the smaller bar
        # keep track of area
        # if curr area larger that max area, replace and move on

        def calc_area(i, j):
            return (j-i) * (heights[i] if heights[i] < heights[j] else heights[j])

        p1, p2 = 0, len(heights) - 1
        max_area = 0
        while p1 < p2:
            curr_area = calc_area(p1, p2)
            max_area = max(max_area, curr_area)

            if heights[p1] > heights[p2]:
                p2-=1
            else:
                p1+=1
        
        return max_area
