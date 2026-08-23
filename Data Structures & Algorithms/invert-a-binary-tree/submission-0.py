# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(curr):
            if not curr:
                return
            
            dfs(curr.right)
            dfs(curr.left)
            curr.right, curr.left = curr.left, curr.right
        
        dfs(root)
        return root