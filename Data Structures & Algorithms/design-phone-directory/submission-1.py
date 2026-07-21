class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        self.max_numbers = maxNumbers
        self.reserved = set()
        self.free = set([i for i in range(self.max_numbers)])

    def get(self) -> int:
        if len(self.free) == 0:
            return -1
        temp = self.free.pop()
        self.reserved.add(temp)
        return temp
        

    def check(self, number: int) -> bool:
        return number in self.free
        

    def release(self, number: int) -> None:
        if number in self.reserved:
            self.reserved.remove(number)
            self.free.add(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
