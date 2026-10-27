"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        active = []
        m = 0
        intervals.sort(key=lambda t: t.start)
        for i in intervals:
            u,v = i.start, i.end
            if active and u >= active[0]:
                heapq.heappop(active)
            heapq.heappush(active, v)
            m = max(m, len(active))
        return m