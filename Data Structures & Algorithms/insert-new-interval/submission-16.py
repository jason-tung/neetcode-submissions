class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        a,b = newInterval
        i = 0
        while i < len(intervals):
            u,v = intervals[i]
            # cases: can insert newinterval, can insert existing interval, can merge
            if b < u:
                res.append([a,b])
                a = b = math.inf
            elif v < a:
                res.append(intervals[i])
                i += 1
            else:
                a,b = min(a,u), max(b, v)
                i += 1
        if a != math.inf:
            res.append([a,b])
        return res
