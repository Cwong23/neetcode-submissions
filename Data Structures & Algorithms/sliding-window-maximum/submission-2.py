import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [-nums[i] for i in range(k)]
        heapq.heapify(heap)
        left, right = 0, k - 1
        res = []
        valid = {}
        for n in heap:
            valid[n] = valid.get(n, 0) + 1
            
        while right < len(nums) - 1:
            while valid[heap[0]] == 0:
                heapq.heappop(heap)
            res.append(-heap[0])
            right+=1
            heapq.heappush(heap, -nums[right])
            valid[-nums[right]] = valid.get(-nums[right], 0) + 1
            valid[-nums[left]]-=1
            left+=1

        while valid[heap[0]] == 0:
                heapq.heappop(heap)
        res.append(-heap[0])

        return res
