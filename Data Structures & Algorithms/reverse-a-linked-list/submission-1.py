# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev: Optional[Node] = None
        curr: Optional[Node] = head


        # a -> b -> c

        while curr != None:
            tmp: Optional[Node] = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev