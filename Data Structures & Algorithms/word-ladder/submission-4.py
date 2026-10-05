class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = defaultdict(list)
        if endWord not in wordList:
            return 0
        for word in wordList:
            for i in range(len(word)):
                pattern = f'{word[:i]}*{word[i+1:]}'
                d[pattern].append(word)
        q = [beginWord]
        next_q = []
        moves = 1
        while q:
            word = q.pop()
            if word == endWord:
                return moves
            for i in range(len(word)):
                pattern = f'{word[:i]}*{word[i+1:]}'
                for word2 in d[pattern]:
                    next_q.append(word2)
                d[pattern] = []
            if not q:
                q, next_q = next_q, []
                moves += 1
        return 0