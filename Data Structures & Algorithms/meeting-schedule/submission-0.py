"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda k: (k.start, k.end))
        n = 0
        for k in intervals:
            if k.start < n:
                return False
            n = k.end
        return True