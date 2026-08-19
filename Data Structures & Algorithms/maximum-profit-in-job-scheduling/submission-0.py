class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        all_items = [[startTime[i], endTime[i], profit[i]] for i in range(n)]
        all_items.sort()
        cache = {}
        
        def dfs(i):
            if i == n:
                return 0
            if i in cache:
                return cache[i]
            
            res = dfs(i+1)

            j = i + 1
            while j < n:
                if all_items[i][1] <= all_items[j][0]:
                    break
                j += 1
            cache[i] = res = max(res, all_items[i][2] + dfs(j))
            return res

        return dfs(0)

"""

finding all combination of jobs where there are no overlaps
we can either take or leave a job, then we are sacrificing
whatever jobs end up in that interval

memoize the previous iterations?

"""
