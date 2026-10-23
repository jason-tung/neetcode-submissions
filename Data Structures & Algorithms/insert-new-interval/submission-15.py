class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        a,b = newInterval
        inserted = False
        for i in range(len(intervals)):
            u,v = intervals[i]
            # 3 cases: can insert (no overlap), no overlap cant insert, overlap
            if b < u and not inserted:
                res.append([a,b])
                inserted = True
                res.append(intervals[i])
            elif a > v or inserted:
                res.append(intervals[i])
            else:
                a,b = min(a,u), max(b,v)
        if not inserted:
            res.append([a,b])
        return res
