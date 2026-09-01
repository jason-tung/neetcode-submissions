class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i,c in enumerate(s):
            d[c] = i
        res = []
        sz, j = 0, 0
        for i,c in enumerate(s):
            sz += 1
            j = max(d[c], j)
            if i == j:
                res.append(sz)
                sz = 0
        return res