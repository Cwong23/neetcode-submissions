class TreeNode:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for x in word:
            if x not in curr.children:
                curr.children[x] = TreeNode()
            curr = curr.children[x]
        curr.word = True


    def search(self, word: str) -> bool:
        curr = self.root
        for x in word:
            if x not in curr.children:
                return False
            curr = curr.children[x]
        return curr.word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for x in prefix:
            if x not in curr.children:
                return False
            curr = curr.children[x]
        return True
        
        