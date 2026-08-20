import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for p in points:
            dist = ((p[0]**2) + (p[1]**2)) ** 0.5
            heapq.heappush(min_heap, (dist, p[0], p[1]))
        res = []
        for i in range(k):
            curr = heapq.heappop(min_heap)
            res.append([curr[1], curr[2]])
        return res