# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while True:
            if fast and fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return False

            if fast == slow:
                return True    
        