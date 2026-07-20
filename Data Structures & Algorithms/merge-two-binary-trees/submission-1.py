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
            
            val = 0
            temp1_left = None
            temp1_right = None
            temp2_left = None
            temp2_right = None
            if curr1:
                val+=curr1.val
                temp1_left = curr1.left
                temp1_right = curr1.right
            if curr2:
                val+=curr2.val
                temp2_left = curr2.left
                temp2_right = curr2.right

            temp = TreeNode(val=val)
            temp.left = dfs(temp1_left, temp2_left)
            temp.right = dfs(temp1_right, temp2_right)
            return temp
        return dfs(root1, root2)
                