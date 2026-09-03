"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        t = defaultdict(int)
        for it in intervals:
            t[it.start] += 1
            t[it.end] -= 1
        meetings = 0
        res = 0
        for time in sorted(t.keys()):
            meetings += t[time]
            res = max(res, meetings)
        return res
