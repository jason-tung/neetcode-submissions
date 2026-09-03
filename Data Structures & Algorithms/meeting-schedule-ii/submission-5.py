"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        soonest_ends = []
        intervals.sort(key=lambda k:k.start)
        for k in intervals:
            s,e = k.start, k.end
            if soonest_ends and s >= soonest_ends[0]:
                heapq.heappop(soonest_ends)
            heapq.heappush(soonest_ends, e)
        return len(soonest_ends)