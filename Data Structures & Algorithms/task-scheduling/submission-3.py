import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        m = {}
        for t in tasks:
            m[t] = m.get(t, 0) + 1
        h = [[0, -v] for v in m.values()]
        heapq.heapify(h)
        while h:
            item = heapq.heappop(h)
            if res < item[0]:
                res = item[0]
            res+=1
            item[1]+=1
            item[0]+=n+1
            if item[1] != 0:
                heapq.heappush(h, item)
        return res