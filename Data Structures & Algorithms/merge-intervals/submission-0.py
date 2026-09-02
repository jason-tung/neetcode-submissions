class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for it in intervals:
            if res and res[-1][0] <= it[1] and it[0] <= res[-1][1]:
                p = res.pop()
                res.append([min(p[0], it[0]), max(p[1], it[1])])
            else:
                res.append(it)
        return res