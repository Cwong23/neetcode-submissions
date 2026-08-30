# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            res_curr = []
            for i in range(size):
                curr = queue.popleft()
                if curr:
                    res_curr.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if res_curr:
                res.append(res_curr)
        
        return res