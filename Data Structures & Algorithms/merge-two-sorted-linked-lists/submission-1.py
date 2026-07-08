# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        if not curr1:
            return curr2
        if not curr2:
            return curr1

        root = None
        if curr1.val < curr2.val:
            root = curr1
            curr1 = curr1.next
        else:
            root = curr2
            curr2 = curr2.next
        curr = root

        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next                

        if curr1:
            while curr1:
                curr.next = curr1
                curr1 = curr1.next 
                curr = curr.next
        elif curr2:
            while curr2:
                curr.next = curr2
                curr2 = curr2.next 
                curr = curr.next

        return root

        