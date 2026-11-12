class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = f'{word[:i]}*{word[i+1:]}'
                d[pattern].append(word)
        q = deque([(1,beginWord)])
        while q:
            cost, word = q.popleft()
            if word == endWord:
                return cost
            for i in range(len(word)):
                pattern = f'{word[:i]}*{word[i+1:]}'
                while d[pattern]:
                    q.append((cost + 1, d[pattern].pop()))                    
        return 0