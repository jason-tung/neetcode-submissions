class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()
        res = []
        a,b = newInterval
        for i, (u, v) in enumerate(intervals):
            if b < u:
                res.append([a,b])
                a = b = math.inf
            if min(b, v) - max(a, u) >= 0:
                a,b = min(a,u), max(b,v)
            else:
                res.append(intervals[i])
        if a != math.inf:
            res.append([a,b])
        return res
                