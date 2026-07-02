import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums[:]
        heapq.heapify(self.nums) 

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        temp = []
        for i in range(len(self.nums) - self.k):
            temp.append(heapq.heappop(self.nums))
        y = self.nums[0]
        for x in temp:
            heapq.heappush(self.nums, x)
        return y
        
