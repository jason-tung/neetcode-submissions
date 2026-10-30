"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda t: t.start)
        end = 0
        for t in intervals:
            a,b = t.start, t.end
            if a < end:
                return False
            end = b
        return True