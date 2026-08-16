# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache: dict[TreeNode, int] = {}

        def dfs(curr):
            if not curr:
                return 0
            if curr in cache:
                return cache[curr]
            
            skip = dfs(curr.left) + dfs(curr.right)
            take = curr.val
            if curr.left:
                take+=dfs(curr.left.left)+dfs(curr.left.right)
            if curr.right:
                take+=dfs(curr.right.left)+dfs(curr.right.right)
            cache[curr] = max(take, skip)
            return cache[curr]

        dfs(root)
        return cache[root]

"""

House robber with binary tree

Max amount of money thief can rob w/o alerting the police in a binary tree
Can't hit two directly linked houses

Heap type data structure so O(1) look up of nodes?
Hash map key: node value: max path

State: A node in the tree
Means: Maximum value at a path
Needs: what are the maximum values below it and what are the maximum values below that
Choice: either take or skip, skipping looks at child nodes vs skipping looks at child child and current
Combine: take max of the two choices and store that

"""