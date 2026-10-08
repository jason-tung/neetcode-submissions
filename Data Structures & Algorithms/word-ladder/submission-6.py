class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = f'{word[:i]}*{word[i+1:]}'
                d[pattern].append(word)
        q = deque([(beginWord, 1)])
        while q:
            word, depth = q.popleft()
            if word == endWord:
                return depth
            for i in range(len(word)):
                pattern = f'{word[:i]}*{word[i+1:]}'
                for newWord in d[pattern]:
                    q.append((newWord, depth + 1))
                d[pattern] = []
        return 0
        

