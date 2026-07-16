class DoubleLinkedNode:
    def __init__(self, val, key=-1, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.mem = {}
        self.cap = capacity
        self.size = 0
        self.head = DoubleLinkedNode(val=0)
        self.tail = DoubleLinkedNode(val=0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.mem:
            return -1
        
        val = self.remove(key)
        self.insert(key, val)
        return self.mem[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.mem:
            self.remove(key)
            self.insert(key, value)
            return
        else:
            if self.size < self.cap:
                self.size+=1
                self.insert(key, value)
                return
            self.remove(self.head.next.key)
            self.insert(key, value)
            return

    def insert(self, key: int, value: int):
        temp = self.tail.prev
        n = DoubleLinkedNode(val=value, key=key, prev=temp, next=self.tail)
        self.mem[key] = n
        temp.next = n
        self.tail.prev = n
        return

    def remove(self, key):
        node = self.mem[key]
        del self.mem[key]
        node.prev.next, node.next.prev = node.next, node.prev
        node.next = None
        node.prev = None
        return node.val

