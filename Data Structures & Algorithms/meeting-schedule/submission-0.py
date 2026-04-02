"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            for j in range(i+1, len(intervals)):
                i1, i2 = intervals[i], intervals[j]
                
                if i1.start < i2.start:
                    if i1.end > i2.start:
                        return False
                elif i1.start > i2.start:
                    if i2.end > i1.start:
                        return False
                else:
                    return False
        return True


