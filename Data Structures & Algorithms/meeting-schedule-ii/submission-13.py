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
        intervals.sort(key=lambda i: i.start)
        m = 0
        for i in intervals:
            a,b = i.start, i.end
            if active and a >= active[0]:
                heapq.heappop(active)
            heapq.heappush(active, b)
            m = max(m, len(active))
        return m