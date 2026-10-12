class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        n,m = len(wordList), len(beginWord)
        d = defaultdict(list)
        for i in range(n):
            for j in range(i+1,n):
                diff = 0
                for c in range(m):
                    if wordList[i][c] != wordList[j][c]:
                        diff += 1
                if diff == 1:
                    d[wordList[i]].append(wordList[j])
                    d[wordList[j]].append(wordList[i])
        q = deque([(beginWord, 1)])
        while q:
            word, cost = q.popleft()
            if word == endWord:
                return cost
            for word2 in d[word]:
                q.append((word2, cost + 1))
            d[word] = []
        return 0