"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        end = 0
        intervals.sort(key=lambda i: i.start)
        for i in intervals:
            u,v = i.start, i.end
            if u < end:
                return False
            end = v
        return True