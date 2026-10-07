# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return (0, None)

            res_l, node_l = dfs(node.left)
            if res_l == 2:
                return (res_l, node_l)
            
            res_r, node_r = dfs(node.right)
            if res_r == 2:
                return (res_r, node_r)
            print("RES: ", res_r, res_l, node.val)
            temp = node if node.val == p.val or node.val == q.val else None
            if temp:
                if res_l == 0 and res_r == 0:
                    return (1, None)
                else:
                    return (2, temp)
            else:
                if res_l == 0 and res_r == 0:
                    return (0, None)
                elif res_l != res_r:
                    return (1, None)
                else:
                    return (2, node)
        _, res = dfs(root)
        return res