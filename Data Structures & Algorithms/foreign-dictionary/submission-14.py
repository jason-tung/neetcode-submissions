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
                for a,b in zip(w1, w2):
                    if a != b:
                        if b not in adj[a]:
                            adj[a].add(b)
                            in_counts[b] += 1
                        break
                else:
                    if len(w1) > len(w2):
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
        
