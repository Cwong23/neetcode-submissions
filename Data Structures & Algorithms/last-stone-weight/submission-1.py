import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [x * -1 for x in stones]
        heapq.heapify(stones)

        while stones and len(stones) > 1:
            largest = heapq.heappop(stones)
            largest_2 = heapq.heappop(stones)

            if largest == largest_2:
                continue
            heapq.heappush(stones, largest - largest_2)
        
        if stones:
            return stones[0] * -1
        return 0