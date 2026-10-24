"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        d = defaultdict(int)
        m = 0
        cur_rooms = 0
        for t in intervals:
            d[t.start] += 1
            d[t.end] -= 1
        for time in sorted(d.keys()):
            cur_rooms += d[time]
            m = max(m, cur_rooms)
        return m