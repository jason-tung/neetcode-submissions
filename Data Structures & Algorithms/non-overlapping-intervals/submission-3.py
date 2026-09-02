class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count, min_end = -1, math.inf
        for start, end in intervals:
            if start < min_end:
                min_end = min(min_end, end)
                count += 1
            else:
                min_end = end
        return max(0, count)