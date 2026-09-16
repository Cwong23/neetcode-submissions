class Logger:

    def __init__(self):
        self.seen: dict[str, int] = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # seen
        if message in self.seen.keys():
            old: int = self.seen[message]
            diff: int = timestamp - old
            
            if diff < 10:
                return False
        
        # not seen
        self.seen[message] = timestamp
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
