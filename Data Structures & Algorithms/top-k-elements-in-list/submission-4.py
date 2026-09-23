import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n]+=1
        
        heap = []
        
        for x,v in freq.items():
            heapq.heappush(heap, [-v, x])
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res