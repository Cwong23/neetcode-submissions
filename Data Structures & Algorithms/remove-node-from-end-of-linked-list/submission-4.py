# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # need to somehow know the end and also the position of the nth node
        # could traverse the list initially to figure out the end and work backwards from there
        # that seems inefficient
        
        # math problem?
        # fast and slow pointers?
        
        # figure out length of list
        # len - n = position relevative to start
        # traverse and remove node

        ptr = head
        length = 0
        while ptr:
            ptr = ptr.next
            length+=1
        
        if length == 1:
            return None

        if length <= 2:
            if n == 1:
                head.next = None
                return head
            return head.next

        pos = length - n

        if pos == 0:
            return head.next

        ptr = head
        for i in range(pos - 1):
            ptr = ptr.next
        
        if ptr.next and ptr.next.next:
            ptr.next = ptr.next.next
        else:
            ptr.next = None
        
        print(head)

        print(pos)
        print(ptr.val)

        return head