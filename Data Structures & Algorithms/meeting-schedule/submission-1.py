"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda k: k.start)
        prev_e = -math.inf
        for k in intervals:
            s,e = k.start, k.end
            if s < prev_e:
                return False
            else:
                prev_e = e
        return True