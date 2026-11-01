class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.word = False

class WordDictionary:

    def __init__(self):
      self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = True

    def search(self, word: str) -> bool:
        def search_dfs(node, idx) -> bool:
            if idx == len(word):
                return node.word

            c = word[idx]

            if c != ".":
                if c not in node.children:
                    return False
                return search_dfs(node.children[c], idx+1)
            for child in node.children.values():
                if search_dfs(child, idx+1):
                    return True
            return False
        return search_dfs(self.trie, 0)                