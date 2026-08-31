class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = Counter(s)
        res = []
        cur = set()
        i = 0
        last = 0
        while i < len(s):
            d[s[i]] -= 1
            if d[s[i]] > 0:
                cur.add(s[i])
                while cur and i < len(s) - 1:
                    i += 1
                    cur.add(s[i])
                    d[s[i]] -= 1
                    if d[s[i]] == 0:
                        cur.remove(s[i])
            res.append(i - last + 1)     
            i += 1
            last = i 
        return res

