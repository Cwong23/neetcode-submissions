class TreeNode:
    def __init__(self):
        self.c = {}
        self.sentence = False
        self.occurances = 0

class Trie:
    def __init__(self):
        self.root = TreeNode()
    
    def input(self, word: str, o=1):
        curr = self.root
        for x in word:
            if x not in curr.c:
                curr.c[x] = TreeNode()
            curr = curr.c[x]
        curr.occurances+=o
        curr.sentence = True
    
    def dfs(self, curr, sentence):
        res = []
        for k, v in curr.c.items():
            res.extend(self.dfs(v, sentence + k))
        if curr.sentence:
            res.append((sentence, curr.occurances))
        return res

    def search_sentences(self, sentence: str):
        curr = self.root
        for x in sentence:
            if x not in curr.c:
                return []
            curr = curr.c[x]
        res = self.dfs(curr, sentence)
        res.sort(key=lambda x: (-x[1], x[0]))
        return [x[0] for x in res[:3]]


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.tree = Trie()
        self.sentence = ""
        for i in range(len(sentences)):
            self.tree.input(sentences[i], times[i])

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.tree.input(self.sentence)
            self.sentence = ""
            return []
        self.sentence+=c
        return self.tree.search_sentences(self.sentence)
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
