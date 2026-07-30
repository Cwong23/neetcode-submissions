# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        temp = []
        def dfs(curr) -> bool:
            if not curr.left and not curr.right:
                temp.append(curr.val)
                return True
                         
            if curr.left:
                if dfs(curr.left):
                    curr.left = None
            if curr.right:
                if dfs(curr.right):
                    curr.right = None
        
        x = False
        while not x:
            x = dfs(root)
            res.append(temp[:])
            temp = []

        return res