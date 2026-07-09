# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # two pointers
        # somehow keep track of both the n-1 and the 1 position at the same time

        # use fast and slow pointer to get to a pointer to the middle of the list
        # reverse 2nd half of the list
        # merge the two lists

        # get to middle
        if not head.next:
            return
        slow, fast = head, head.next.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        if fast:
            slow = slow.next
        
        # break off the lists
        temp = slow
        slow = slow.next
        temp.next = None

        # reverse the linked list
        prev, curr = slow, slow.next
        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        l, r = head, prev

        # print("l")
        # while l:
        #     print(l.val)
        #     l = l.next

        # print("r")
        # while r:
        #     print(r.val)
        #     r = r.next

        # merge lists
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




        h = head
        print("h")
        while h:
            print(h.val)
            h = h.next

        return



