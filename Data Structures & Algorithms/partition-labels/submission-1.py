class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i,c in enumerate(s):
            d[c] = i
        res = []
        sz, i, j = 1, 0, 0
        while i < len(s):
            sz = 1
            c = s[i]
            j = d[c]
            while i < j:
                j = max(j, d[s[i]])
                i += 1
                sz += 1
            res.append(sz)
            i += 1
        return res