class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        letters = set(l for word in words for l in word)
        res = []
        edges = defaultdict(set)
        in_count = defaultdict(int)
        for i in range(n - 1):
            word1, word2 = words[i], words[i+1]
            for a,b in zip(word1, word2):
                if a != b:
                    in_count[b] += 1 if b not in edges[a] else 0
                    edges[a].add(b)
                    break
            else:
                if len(word1) > len(word2):
                    return ''
        stack = [l for l in letters if not in_count[l]]
        while stack:
            l = stack.pop()
            letters.remove(l)
            res.append(l)
            for l2 in edges[l]:
                in_count[l2] -= 1
                if not in_count[l2]:
                    stack.append(l2)
        return ''.join(res) if not len(letters) else ''
        
            