"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda t: (t.start, t.end))
        pq = []
        m = 0
        for t in intervals:
            u,v = t.start, t.end
            if pq and u >= pq[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, v)
            m = max(m, len(pq))
        return m