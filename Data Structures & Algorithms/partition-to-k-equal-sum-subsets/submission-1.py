class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < k:
            return False

        sum_nums = sum(nums)
        if sum_nums % k != 0:
            return False
        partition = sum_nums / k
        cache = {}
        nums.sort(reverse=True)
        if nums[0] > partition:
            return False
        subsets = [0] * k

        def dfs(i):
            if i == n:
                return all(s == partition for s in subsets)
            key = (i, tuple(sorted(subsets)))
            if key in cache:
                return cache[key]
            
            for j in range(k):
                if subsets[j] + nums[i] <= partition:
                    subsets[j]+=nums[i]
                    if dfs(i+1):
                        cache[key] = True
                        return True
                    subsets[j]-=nums[i]
            cache[key] = False
            return False                    

        return dfs(0)
