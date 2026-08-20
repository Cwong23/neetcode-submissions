import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        res = 0
        q = deque()
        while max_heap or q:
            res+=1

            if not max_heap:
                res = q[0][1]
            else:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt, res + n])
            if q and q[0][1] == res:
                heapq.heappush(max_heap, q.popleft()[0])

        return res
            