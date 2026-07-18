class PrefixTree:

    def __init__(self):
        self.end = False
        self.children = {}

    def insert(self, word: str) -> None:
        def seek_ins(node, i):
            if i == len(word):
                node.end = True
                return
            if word[i] not in node.children:
                node.children[word[i]] = PrefixTree()
            seek_ins(node.children[word[i]], i + 1)
        seek_ins(self, 0)

    def search(self, word: str) -> bool:
        def seek(node, i):
            if i == len(word):
                return node.end
            if word[i] not in node.children:
                return False
            return seek(node.children[word[i]], i + 1)
        return seek(self, 0)

    def startsWith(self, prefix: str) -> bool:
        def seek(node, i):
            if i == len(prefix):
                return True
            if prefix[i] not in node.children:
                return False
            return seek(node.children[prefix[i]], i + 1)
        return seek(self, 0)
        