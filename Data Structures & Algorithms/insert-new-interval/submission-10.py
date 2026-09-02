class Solution:
    def insert(self, intervals: List[List[int]], tar: List[int]) -> List[List[int]]:
        res = []
        for (i,interval) in enumerate(intervals):
            if interval[1] < tar[0]:
                res.append(interval)
            elif tar[1] >= interval[0]:
                tar = [min(tar[0], interval[0]), max(tar[1], interval[1])]
            else:
                res.append(tar)
                res.extend(intervals[i:])
                return res
        res.append(tar)
        return res