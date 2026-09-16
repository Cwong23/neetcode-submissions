from collections import deque

class HitCounter:

    def __init__(self):
        self.system: deque[int] = deque()
        

    def hit(self, timestamp: int) -> None:
        self.system.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.system:
            # peek
            diff: int = timestamp - self.system[0]
            if diff >= 300:
                self.system.popleft()
            else:
                break

        return len(self.system)
        
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
