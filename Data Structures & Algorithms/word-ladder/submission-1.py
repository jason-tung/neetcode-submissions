class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        d = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                wild = f'{word[:i]}*{word[i+1:]}'
                d[wild].append(word)
        visited = set([beginWord])
        q = deque([(beginWord, 1)])
        while q:
            word, moves = q.popleft()
            if word == endWord:
                return moves
            for i in range(len(word)):
                wild = f'{word[:i]}*{word[i+1:]}'
                for w2 in d[wild]:
                    if w2 not in visited:
                        visited.add(w2)
                        q.append((w2, moves + 1))
                d[wild] = []
        return 0
