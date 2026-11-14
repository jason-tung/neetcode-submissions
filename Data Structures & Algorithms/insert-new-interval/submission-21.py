class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        a,b = newInterval
        intervals.sort()
        res = []
        for i in range(len(intervals)):
            u,v = intervals[i]
            if b < u:
                res.append([a,b])
                a = b = math.inf
            if a > v:
                res.append(intervals[i])
            else:
                a, b = min(a, u), max(b, v)
        if a != math.inf:
            res.append([a,b])
        return res