# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr, left, right):
            if not curr:
                return True
            if not (left < curr.val < right):
                return False

            return dfs(curr.left, left, curr.val) and dfs(
                curr.right, curr.val, right
            )

        return dfs(root, float("-inf"), float("inf"))