# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(curr, smaller, greater):
            if curr == None:
                return None
            if curr.val >= smaller and curr.val <= greater:
                return curr
            
            if curr.val > smaller and curr.val > greater:
                return dfs(curr.left, smaller, greater)
            return dfs(curr.right, smaller, greater)

        a = p.val if p.val < q.val else q.val
        b = p.val if p.val > q.val else q.val
        node = dfs(root, a, b)
        return node