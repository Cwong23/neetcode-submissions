# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def find_min():
            i = 0
            while not lists[i]:
                i+=1
                if i >= len(lists):
                    return None
            min_ptr = lists[i]
            idx = i
            for i, node_list in enumerate(lists):
                if node_list and node_list.val < min_ptr.val:
                    min_ptr = node_list
                    idx = i
            lists[idx] = lists[idx].next
            return min_ptr
        
        head = find_min()
        res = head

        while lists:
            temp = find_min()
            if temp:
                head.next = temp
                head = head.next
            else:
                break

        return res