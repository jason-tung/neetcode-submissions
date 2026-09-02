class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count, max_end = -1, math.inf
        for start, end in intervals:
            if start < max_end:
                max_end = min(max_end, end)
                count += 1
            else:
                max_end = end
        return max(0, count)