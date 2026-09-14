import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        tasks_sorted = [[x[1], i, x[0]] for i, x in enumerate(tasks)]
        tasks_sorted.sort(key=lambda x: x[2])
        res = []
        time = 1
        ptr = 0
        max_time = tasks_sorted[-1][2]

        while time < max_time or ptr < len(tasks):
            temp = ptr
            while ptr < len(tasks) and tasks_sorted[ptr][2] <= time:
                heapq.heappush(heap, tasks_sorted[ptr])
                ptr+=1
            if temp == ptr:
                time+=1
                continue
            curr = heapq.heappop(heap)
            time += curr[0]
            res.append(curr[1])

        while len(heap) != 0:
            curr = heapq.heappop(heap)
            res.append(curr[1])

        return res
        