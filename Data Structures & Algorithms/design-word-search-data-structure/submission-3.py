class WordDictionary:

    def __init__(self):
        self.end = False
        self.children = {}

    def addWord(self, word: str) -> None:
        def add(node, i):
            if i == len(word):
                node.end = True
            else:
                if word[i] not in node.children:
                    node.children[word[i]] = WordDictionary()
                add(node.children[word[i]], i + 1)
        add(self, 0)

    def search(self, word: str) -> bool:
        def seek(node, i):
            if i == len(word):
                return node.end
            c = word[i]
            if c != '.':
                if c not in node.children:
                    return False
                return seek(node.children[c], i + 1)
            else:
                for k in node.children:
                    if seek(node.children[k], i + 1):
                        return True
            return False
        return seek(self, 0)
        
