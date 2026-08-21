import heapq

class MedianFinder:

    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.left_max_heap) == len(self.right_min_heap):
            if self.left_max_heap and self.right_min_heap:
                if self.right_min_heap[0] >= num:
                    heapq.heappush(self.left_max_heap, -num)
                else:
                    heapq.heappush(self.right_min_heap, num)
            else:
                heapq.heappush(self.left_max_heap, -num)
        else:
            if len(self.right_min_heap) > len(self.left_max_heap) or not self.left_max_heap:
                if num > self.right_min_heap[0]:
                    heapq.heappush(self.left_max_heap, -heapq.heappop(self.right_min_heap))
                    heapq.heappush(self.right_min_heap, num)
                else:
                    heapq.heappush(self.left_max_heap, -num)
            else:
                if num < -self.left_max_heap[0]:
                    heapq.heappush(self.right_min_heap, -heapq.heappop(self.left_max_heap))
                    heapq.heappush(self.left_max_heap, -num)
                else:
                    heapq.heappush(self.right_min_heap, num)

    def findMedian(self) -> float:
        if len(self.right_min_heap) == len(self.left_max_heap):
            return (self.right_min_heap[0] - self.left_max_heap[0]) / 2
        elif len(self.right_min_heap) > len(self.left_max_heap):
            return self.right_min_heap[0]
        return -self.left_max_heap[0]