# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(h):
            prev = h
            h = h.next
            prev.next = None
            while h:
                temp = h.next
                h.next = prev
                prev = h
                h = temp
            return prev
        
        def disconnect_and_reverse(head, tail):
            temp = None
            if tail:
                temp = tail.next
                tail.next = None
            h = reverse(head)
            head.next = temp
            return h
        
        def reverse_k_nodes(curr):
            h = curr
            i = 0
            while i < k - 1:
                if curr == None:
                    return None
                curr = curr.next
                i+=1
            else:
                if curr == None:
                    return h
                h = disconnect_and_reverse(h, curr)
                return h

        og = head
        h = reverse_k_nodes(head)
        l = h

        while True:
            temp = og.next
            l = reverse_k_nodes(temp)
            if not l:
                break
            og.next = l
            og = temp

        return h