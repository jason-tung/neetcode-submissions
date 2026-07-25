class Trie:
    def __init__(self):
        self.end=False
        self.word=None
        self.children = {}
    
    def insert(self, word):
        def ins(node, i):
            if i >= len(word):
                node.end = True
                node.word = word
            else:
                if word[i] not in node.children:
                    node.children[word[i]] = Trie()
                ins(node.children[word[i]], i + 1)
        ins(self, 0)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for k in words:
            trie.insert(k)
        solved = set()
        def dfs_closure(r,c):
            visited = set()
            node = trie
            def dfs(r,c):
                if (r,c) not in visited and 0 <= r < len(board) and 0 <= c < len(board[0]):
                    char = board[r][c]
                    visited.add((r,c))
                    nonlocal node
                    if char in node.children:
                        next_node = node.children[char]
                        if next_node.end:
                            solved.add(next_node.word)
                        for d in [(0,1), (0,-1), (1,0), (-1,0)]:
                            node = next_node
                            dfs(r+d[0], c+d[1])
                    visited.remove((r,c))
            dfs(r,c)
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs_closure(r,c)

        return list(solved)
        