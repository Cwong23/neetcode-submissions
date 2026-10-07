import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapq.heapify(h)

        while True:
            if not h:
                return 0
            st1 = heapq.heappop(h)
            if not h:
                return -st1
            st2 = heapq.heappop(h)
            if st1 == st2:
                continue
            winner = st1 - st2
            heapq.heappush(h, winner)
        return 0