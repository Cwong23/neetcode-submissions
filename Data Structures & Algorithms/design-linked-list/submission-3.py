class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next: ListNode | None = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.length: int = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        
        curr = self.head.next
        count: int = 0
        while curr is not None:
            if index == count:
                return curr.val

            curr = curr.next
            count += 1
        
        return -1
        

    def addAtHead(self, val: int) -> None:
        tmp: ListNode = ListNode(val)
        tmp.next = self.head.next
        self.head.next = tmp
        self.length += 1

    def addAtTail(self, val: int) -> None:
        tmp: ListNode = ListNode(val)
        curr = self.head

        while curr.next is not None:
            curr = curr.next
        
        curr.next = tmp
        self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length or index < 0:
            return

        curr = self.head
        count: int = 0
        while curr is not None:
            if index == count:
                tmp: ListNode = ListNode(val)
                tmp.next = curr.next
                curr.next = tmp
                self.length += 1
                return

            curr = curr.next        
            count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index > self.length or index < 0:
            return

        curr = self.head
        count: int = 0

        while curr.next is not None:
            if index == count:
                curr.next = curr.next.next
                self.length -= 1
                return

            curr = curr.next        
            count += 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)