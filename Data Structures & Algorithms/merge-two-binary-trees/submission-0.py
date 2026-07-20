# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(curr1, curr2) -> Optional[TreeNode]:
            if not curr1 and not curr2:
                return None
            elif curr1 and curr2:
                temp = TreeNode(val=curr1.val+curr2.val)
                temp.left = dfs(curr1.left, curr2.left)
                temp.right = dfs(curr1.right, curr2.right)
                return temp
            elif curr1 and not curr2:
                temp = TreeNode(val=curr1.val)
                temp.left = dfs(curr1.left, None)
                temp.right = dfs(curr1.right, None)
                return temp
            temp = TreeNode(val=curr2.val)
            temp.left = dfs(None, curr2.left)
            temp.right = dfs(None, curr2.right)
            return temp
        return dfs(root1, root2)
                