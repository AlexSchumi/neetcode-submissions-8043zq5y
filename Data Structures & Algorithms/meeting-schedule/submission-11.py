"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        if len(sorted_intervals) <= 1:
            return True
        prev_end = sorted_intervals[0].end
        
        for i in range(1, len(intervals)):
            cur_start = sorted_intervals[i].start
            if cur_start < prev_end:
                return False
            else:
                prev_end = sorted_intervals[i].end
        return True

