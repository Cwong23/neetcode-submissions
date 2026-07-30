# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # have a list to contain the all the numbers and then sum them
        # use dfs to figure out the numbers
        # multiple by 10 each time we travel down a node and add the current
        # when a leaf node is reached, stop at add that total number to the list
        if not root:
            return 0

        res = []

        def dfs(curr, curr_int):
            # leaf node is base case
            if not curr.left and not curr.right:
                res.append((curr_int * 10) + curr.val)
                return
            if curr.left:
                dfs(curr.left, curr_int*10 + curr.val)
            if curr.right:
                dfs(curr.right, curr_int*10 + curr.val)
            return
        
        dfs(root, 0)

        return sum(res)