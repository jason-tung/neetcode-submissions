"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        end = 0
        for i in intervals:
            a,b = i.start, i.end
            if a < end:
                return False
            end = b
        return True