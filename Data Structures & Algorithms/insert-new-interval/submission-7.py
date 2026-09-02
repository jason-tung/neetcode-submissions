class Solution:
    def insert(self, intervals: List[List[int]], tar: List[int]) -> List[List[int]]:
        res = []
        i = 0
        while i < len(intervals) and intervals[i][1] < tar[0]:
            res.append(intervals[i])
            i += 1
        while i < len(intervals) and tar[1] >= intervals[i][0] and tar[0] <= intervals[i][1]:
            tar = [min(tar[0], intervals[i][0]), max(tar[1], intervals[i][1])]
            i += 1
        res.append(tar)
        for j in range(i, len(intervals)):
            res.append(intervals[j])
        return res
