"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0
        intervals.sort(key=lambda x: x.start)
        heap = []

        for interval in intervals:
            while heap and heap[0][0] <= interval.start:
                heapq.heappop(heap)
            heapq.heappush(heap, (interval.end, interval.start))
            res = max(len(heap), res)
        return res
