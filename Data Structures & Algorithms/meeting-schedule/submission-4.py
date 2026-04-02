"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort intervals by start time
        intervals.sort(key = lambda x: x.start)

        # find overlap between intervals
        for i in range(1, len(intervals)):
            one, two = intervals[i-1], intervals[i]

            if two.start < one.end:
                return False
        return True