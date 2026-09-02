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

        res = [0]

        def dfs(curr, curr_max):
            if not curr:
                return
            if curr.val >= curr_max:
                curr_max = curr.val
                res[0]+=1
            dfs(curr.left, curr_max)
            dfs(curr.right, curr_max)
            return
        
        dfs(root, root.val)

        return res[0]