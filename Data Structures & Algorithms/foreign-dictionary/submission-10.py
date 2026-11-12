class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        in_counts = Counter()
        letters = set()
        res = []
        for i in range(len(words)):
            for c in words[i]:
                letters.add(c)
            if i < len(words) - 1:
                p1 = p2 = 0
                w1, w2 = words[i], words[i+1]
                while p1 < len(w1) and p2 < len(w2) and w1[p1] == w2[p2]:
                    p1 += 1
                    p2 += 1
                if p1 < len(w1) and p2 >= len(w2):
                    return ''
                if p1 < len(w1) and p2 < len(w2) and w2[p2] not in adj[w1[p1]]:
                    adj[w1[p1]].add(w2[p2])
                    in_counts[w2[p2]] += 1
        q = deque(k for k in letters if not in_counts[k])
        while q:
            node = q.popleft()
            res.append(node)
            for dest in adj[node]:
                in_counts[dest] -= 1
                if not in_counts[dest]:
                    del in_counts[dest]
                    q.append(dest)
        return ''.join(res) if not len(in_counts) else ''
        
