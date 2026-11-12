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
                w1, w2 = words[i], words[i+1]
                has_hit = False
                for j in range(min(len(w1), len(w2))):
                    if w1[j] != w2[j]:
                        if w2[j] not in adj[w1[j]]:
                            adj[w1[j]].add(w2[j])
                            in_counts[w2[j]] += 1
                        has_hit = True
                        break
                if not has_hit and len(w1) > len(w2):
                    return ''
        q = deque(k for k in letters if not in_counts[k])
        while q:
            node = q.popleft()
            res.append(node)
            for dest in adj[node]:
                in_counts[dest] -= 1
                if not in_counts[dest]:
                    q.append(dest)
        return ''.join(res) if len(letters) == len(res) else ''
        
