# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(curr): # should return longest path and longest diameter
            if curr == None:
                return (0, 0)

            left_path, left_diameter = dfs(curr.left)
            right_path, right_diameter = dfs(curr.right)
            curr_diameter = left_path + right_path

            return max(left_path, right_path) + 1, max(curr_diameter, left_diameter, right_diameter)            

        _, d = dfs(root)

        return d