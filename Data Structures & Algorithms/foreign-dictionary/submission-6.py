class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        res = []
        edges = defaultdict(list)
        in_count = defaultdict(int)
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            c = 0
            while c < len(w1) and c < len(w2) and w1[c] == w2[c]:
                c += 1
            if c >= len(w2) and c < len(w1):
                return ""
            if c < len(w1) and c < len(w2):
                edges[w1[c]].append(w2[c])
                in_count[w2[c]] += 1
        letters = set(''.join(words))
        q = [l for l in letters if in_count[l] == 0]
        while q:
            p = q.pop()
            res.append(p)
            for char in edges[p]:
                in_count[char] -= 1
                if in_count[char] == 0:
                    q.append(char)
        if len(res) != len(letters):
            return ""
        return ''.join(res)