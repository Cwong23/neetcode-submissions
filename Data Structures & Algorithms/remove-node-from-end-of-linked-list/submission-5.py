# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
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
        
        return head