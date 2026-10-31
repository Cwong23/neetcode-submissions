# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node, prev):
            if not node:
                return 0
            new_max = max(prev, node.val)
            total = dfs(node.left, new_max) + dfs(node.right, new_max)
            if node.val >= prev:
                total+=1
            return total

        return dfs(root, float('-inf'))