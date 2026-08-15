class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sum_matchsticks = sum(matchsticks)
        if sum_matchsticks % 4 != 0 or len(matchsticks) < 4:
            return False
        partition_size = sum_matchsticks / 4
        cache = set()
        matchsticks.sort(reverse=True)
        n = len(matchsticks)
        sides = [0, 0, 0, 0]

        def dfs(i) -> bool:
            if i == n:
                if sides[0] == sides[1] == sides[2] == sides[3]:
                    return True
                return False
            key = tuple(sides)
            if key in cache:
                return False
            for x in range(4):
                sides[x]+=matchsticks[i]
                if sides[x] <= partition_size:
                    if dfs(i+1):
                        return True
                sides[x]-=matchsticks[i]
            cache.add(key)
            return False
        return dfs(0)

