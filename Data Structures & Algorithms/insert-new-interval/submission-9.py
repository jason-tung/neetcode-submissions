class Solution:
    def insert(self, intervals: List[List[int]], tar: List[int]) -> List[List[int]]:
        res = []
        flagged = False
        for interval in intervals:
            if interval[1] < tar[0]:
                res.append(interval)
            elif tar[1] >= interval[0]:
                tar = [min(tar[0], interval[0]), max(tar[1], interval[1])]
            else:
                if not flagged:
                    flagged = True
                    res.append(tar)
                res.append(interval)
        if not flagged:
                    flagged = True
                    res.append(tar)
        return res