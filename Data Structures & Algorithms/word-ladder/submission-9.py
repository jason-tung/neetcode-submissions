class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = f'{word[:i]}*{word[i+1:]}'
                d[pattern].append(word)
        q = deque([(beginWord, 1)])
        while q:
            word, cost = q.popleft()
            if word == endWord:
                return cost
            for i in range(len(word)):
                pattern = f'{word[:i]}*{word[i+1:]}'
                for word2 in d[pattern]:
                    q.append((word2, cost + 1))
                d[pattern] = []
        return 0