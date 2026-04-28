"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)==0:
            return True
        
        
        intervals.sort(key=lambda i : i.start)
        
        last=intervals[0].start
        for meeting in intervals:
            if meeting.start<last:
                return False
            else:
                last=meeting.end
        return True
