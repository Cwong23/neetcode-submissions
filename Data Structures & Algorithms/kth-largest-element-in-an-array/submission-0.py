import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_heap = []

        for x in nums:
            if len(min_heap) == k:
                if x > min_heap[0]:
                    heapq.heappop(min_heap)
                else:
                    continue
            heapq.heappush(min_heap, x)
        return min_heap[0]