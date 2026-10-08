class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = f'{word[:i]}*{word[i+1:]}'
                d[pattern].append(word)
        q = deque([beginWord])
        next_q = deque()
        depth = 1
        while q:
            word = q.popleft()
            if word == endWord:
                return depth
            for i in range(len(word)):
                pattern = f'{word[:i]}*{word[i+1:]}'
                for newWord in d[pattern]:
                    next_q.append(newWord)
                d[pattern] = []
            if not q:
                depth += 1
                next_q, q = deque(), next_q
        return 0
        

