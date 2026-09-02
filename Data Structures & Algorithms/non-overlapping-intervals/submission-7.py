class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda k:k[1])
        prev_end = -math.inf
        count=0
        for start,end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                count += 1
        return count