# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        slow, fast = head, head.next.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        if fast:
            slow = slow.next
        
        temp = slow
        slow = slow.next
        temp.next = None

        prev, curr = slow, slow.next
        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        l, r = head, prev
        s = l
        l = l.next
        while l and r:
            s.next = r
            r = r.next
            s = s.next
            s.next = l
            l = l.next
            s = s.next
        if r:
            s.next = r
        if l:
            s.next = l
        return
