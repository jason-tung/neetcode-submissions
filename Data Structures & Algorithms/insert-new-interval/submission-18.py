class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()
        res = []
        a,b = newInterval
        for i, (u, v) in enumerate(intervals):
            if b < u:
                res.append([a,b])
                a = b = math.inf
            if a > v:
                res.append(intervals[i])
            else:
                a,b = min(a,u), max(b,v)
        if a != math.inf:
            res.append([a,b])
        return res
                