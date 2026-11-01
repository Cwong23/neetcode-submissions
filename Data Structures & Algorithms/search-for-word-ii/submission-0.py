class TrieNode:
    def __init__(self):
        self.word = False
        self.children: dict[str, TrieNode] = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = True

    def search(self, word):
        def dfs(ptr, node):
            if len(word) == ptr:
                return node.word
            c = word[ptr]
            if c not in node.children:
                return False
            return dfs(ptr+1, node.children[c])
        return dfs(0, self.root)

from collections import deque

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = Trie()
        for word in words:
            tree.add_word(word)
        
        res = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n, m = len(board), len(board[0])

        def dfs(r, c, node, path, visited):
            if not (0 <= r < n and 0 <= c < m):
                return
            if (r, c) in visited:
                return
            if board[r][c] not in node.children:
                return

            node = node.children[board[r][c]]
            path += board[r][c]
            visited.add((r, c))

            if node.word:
                res.add(path)

            for dr, dc in directions:
                dfs(r + dr, c + dc, node, path, visited)

            visited.remove((r, c))

        for i in range(n):
            for j in range(m):
                if board[i][j] in tree.root.children:
                    dfs(i, j, tree.root, "", set())

        return list(res)