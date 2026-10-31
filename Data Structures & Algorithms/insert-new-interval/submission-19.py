class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        a,b = newInterval
        intervals.sort()
        res = []
        for u,v in intervals:
            if b < u:
                res.append([a,b])
                a = b = math.inf
            if v < a:
                res.append([u,v])
            else:
                a,b = min(a,u), max(v,b)
        if a != math.inf:
            res.append([a,b])
        return res