class Logger:

    def __init__(self):
        self.seen: dict[int, int] = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        msg_hash: int = hash(message)

        if self.seen.get(msg_hash) is not None:
            
            # timestamp 100
            # msg_hash 91
            # diff = 9 # NO


            # timestamp 100
            # msg_hash 90
            # diff = 10 # YES

            diff: int = timestamp - self.seen[msg_hash]
            if diff >= 10:
                self.seen[msg_hash] = timestamp
            else:
                return False
        
        else:
            self.seen[msg_hash] = timestamp
        
        return True
        

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
