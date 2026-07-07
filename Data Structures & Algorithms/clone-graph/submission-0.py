"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(curr):
            if not curr:
                return None
            if curr in visited:
                return visited[curr]

            node_copy = Node(curr.val)
            visited[curr] = node_copy
            node_copy.neighbors = [dfs(n) for n in curr.neighbors]

            return node_copy

        node_copy = dfs(node)

        return node_copy