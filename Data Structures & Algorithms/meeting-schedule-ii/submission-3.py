import heapq
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1
        # if there is two
        res = 1
        intervals.sort(key=lambda x: x.start) #sort by start
        rooms_heap = [intervals[0].end]

        for i in range(1, len(intervals)):
            '''
            if interval.start < prev_end:
                res += 1
                prev_end = min(interval.end, prev_end)
            '''
            if intervals[i].start >= rooms_heap[0]:
                heapq.heappop(rooms_heap)
            heapq.heappush(rooms_heap, intervals[i].end)

        return len(rooms_heap)

        