# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare_trees(root, sub_root):
            if not root:
                return True if sub_root is None else False
            if not sub_root:
                return False
            if root.val != sub_root.val:
                return False
            return compare_trees(root.left, sub_root.left) and compare_trees(root.right, sub_root.right)

        def search(root):
            if not root:
                return False
            if root.val == subRoot.val:
                if compare_trees(root, subRoot):
                    return True
            if search(root.left):
                return True
            return search(root.right)

        return search(root)