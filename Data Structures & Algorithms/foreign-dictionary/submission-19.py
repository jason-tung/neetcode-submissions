class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        letters = set(c for w in words for c in w)
        res = []
        adj = defaultdict(set)
        in_count = Counter()
        for i in range(len(words) - 1):
            w1,w2 = words[i], words[i+1]
            has_diff = False
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] in w1[j]:
                        return ""
                    if w2[j] not in adj[w1[j]]:
                        in_count[w2[j]] += 1
                    adj[w1[j]].add(w2[j])
                    has_diff = True
                    break
            if not has_diff and len(w1) > len(w2):
                return ""
        stack = [l for l in letters if in_count[l] == 0]
        while stack:
            letter = stack.pop()
            res.append(letter)
            for l2 in adj[letter]:
                in_count[l2] -= 1
                if in_count[l2] == 0:
                    stack.append(l2)
        return ''.join(res) if len(res) == len(letters) else ""
        
        
