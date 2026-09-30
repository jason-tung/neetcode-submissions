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
            char1 = char2 = "@"
            if c < len(w1):
                char1 = w1[c]
            if c < len(w2):
                char2 = w2[c]
            if char2 == "@": 
                if char1 != "@":
                    return ""
                continue
            if char1 != "@":
                edges[char1].append(char2)
                in_count[char2] += 1
        letters = set(''.join(words))
        q = [l for l in letters if in_count[l] == 0]
        solved = set()
        while q:
            p = q.pop()
            if p in solved:
                return ""
            solved.add(p)
            res.append(p)
            for char in edges[p]:
                in_count[char] -= 1
                if in_count[char] <= 0:
                    if char in solved:
                        return ""
                    q.append(char)
        if len(res) != len(letters):
            return ""
        return ''.join(res)