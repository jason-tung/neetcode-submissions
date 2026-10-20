class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        u,v = newInterval
        for a,b in intervals:
            if b < u or v < a:
                if u < a:
                    res.append([u,v])
                    u = v = math.inf
                res.append([a,b])
            else:
                u,v = min(u,a), max(v,b)
        if u != math.inf:
            res.append([u,v])
        return res
