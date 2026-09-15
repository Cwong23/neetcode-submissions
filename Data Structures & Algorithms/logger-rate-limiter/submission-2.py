class Logger:

    def __init__(self):
        self.seen: dict[str: int] = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # Check existing msgs
        if message in self.seen:
            # Which comes first? timestamp
            diff: int = timestamp - self.seen[message] 
            if diff < 10:
                return False

        # Add fresh msg
        self.seen[message] = timestamp
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
