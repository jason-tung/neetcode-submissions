"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i: i.start)
        h = []
        m = 0
        for i in intervals:
            u,v = i.start, i.end
            if h and u >= h[0]:
                heapq.heappop(h)
            heapq.heappush(h, v)
            m = max(m, len(h))
        return m