class DoubleNode:
    def __init__(self, value: str, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.value = value

class BrowserHistory:
# doubly linked list and hash map?
    def __init__(self, homepage: str):
        self.head = DoubleNode("")
        self.tail = DoubleNode("")
        home = DoubleNode(homepage, prev=self.head, next=self.tail)
        self.tail.prev = home
        self.head.next = home
        self.curr = home
        

    def visit(self, url: str) -> None:
        new = DoubleNode(url, prev=self.curr, next=self.tail)
        self.curr.next = new
        self.tail.prev = new
        self.curr = new

    def back(self, steps: int) -> str:
        i = 0
        while self.curr.prev != self.head and i < steps:
            self.curr = self.curr.prev
            i+=1
        return self.curr.value

    def forward(self, steps: int) -> str:
        i = 0
        while self.curr.next != self.tail and i < steps:
            self.curr = self.curr.next
            i+=1
        return self.curr.value
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)