# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 = []
        stack2 = []

        if p and q:
            stack1.append(p)
            stack2.append(q)
        elif not p and not q:
            return True
        else:
            return False

        while stack1:
            curr_p = stack1.pop()
            curr_q = stack2.pop() 
            if curr_p.val == curr_q.val:
                if (curr_p.left and curr_q.left):
                    stack1.append(curr_p.left)
                    stack2.append(curr_q.left)
                elif (not curr_p.left and not curr_q.left):
                    pass
                else:
                    return False
                if (curr_p.right and curr_q.right):
                    stack1.append(curr_p.right)
                    stack2.append(curr_q.right)
                elif (not curr_p.right and not curr_q.right):
                    pass
                else:
                    return False
            else:
                return False
        return True
