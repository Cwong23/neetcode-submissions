# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(curr) -> int:
            if not curr:
                return 0

            left_path = dfs(curr.left)
            right_path = dfs(curr.right)
            l, r = max(left_path, 0), max(right_path, 0)
            
            res[0] = max(res[0], curr.val + l + r)
            return curr.val + max(l, r)
        dfs(root)
        return res[0]