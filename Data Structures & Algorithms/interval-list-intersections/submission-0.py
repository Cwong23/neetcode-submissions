class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res: list[list[int]] = []
        n, m = len(firstList), len(secondList)
        
        i, j = 0, 0
        while i < n and j < m:
            start_a, end_a = firstList[i]
            start_b, end_b = secondList[j]
            
            start = max(start_a, start_b)
            end = min(end_a, end_b)

            if start <= end:
                res.append([start, end])
            if end_a < end_b:
                i+=1
            else:
                j+=1
        return res
