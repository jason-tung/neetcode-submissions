class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = defaultdict(list)
        wordList.append(beginWord)
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                w1,w2 = wordList[i], wordList[j]
                diff = sum(1 if w1[c] != w2[c] else 0 for c in range(len(w1)))
                if diff <= 1:
                    d[w1].append(w2)
                    d[w2].append(w1)
        visited = set([beginWord])
        q = deque([(beginWord, 1)])
        while q:
            w,m = q.popleft()
            if w == endWord:
                return m
            for k in d[w]:
                if k not in visited:
                    visited.add(k)
                    q.append((k,m+1))
        return 0
