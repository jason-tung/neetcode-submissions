class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda k:-k[0])
        prev_start = math.inf
        count=0
        for start,end in intervals:
            if end > prev_start:
                count += 1
            else:
                prev_start = start
        return count