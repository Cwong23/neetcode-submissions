class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.ptr = 0
        self.uniques = {}
        for n in nums:
            self.uniques[n] = self.uniques.get(n, 0) + 1

    def showFirstUnique(self) -> int:
        while self.ptr < len(self.nums):
            if self.uniques[self.nums[self.ptr]] == 1:
                return self.nums[self.ptr]
            self.ptr+=1
        return -1

    def add(self, value: int) -> None:
        self.nums.append(value)
        self.uniques[value] = self.uniques.get(value, 0) + 1 


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
