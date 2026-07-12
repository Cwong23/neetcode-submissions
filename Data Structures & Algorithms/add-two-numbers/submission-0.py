# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        res = ListNode()
        res_cur = res
        carry_over = 0

        while cur1 and cur2:
            temp = carry_over + cur1.val + cur2.val
            val = temp % 10
            if val != temp:
                carry_over = 1
            else:
                carry_over = 0
            res_cur.val = val
            if cur1.next or cur2.next:
                res_cur.next = ListNode()
                res_cur = res_cur.next
            else:
                res_cur.next = None
            cur1, cur2 = cur1.next, cur2.next

        while cur1:
            temp = carry_over + cur1.val
            val = temp % 10
            if val != temp:
                carry_over = 1
            else:
                carry_over = 0
            res_cur.val = val
            if cur1.next:
                res_cur.next = ListNode()
                res_cur = res_cur.next
            else:
                res_cur.next = None
            cur1 = cur1.next

        while cur2:
            temp = carry_over + cur2.val
            val = temp % 10
            if val != temp:
                carry_over = 1
            else:
                carry_over = 0
            res_cur.val = val
            if cur2.next:
                res_cur.next = ListNode()
                res_cur = res_cur.next
            else:
                res_cur.next = None
            cur2 = cur2.next

        if carry_over != 0:
            res_cur.next = ListNode(val=1)

        return res
