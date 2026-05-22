class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        sorted_intervals = sorted(intervals, key=lambda x: x[0]) # sort start time
        prev_start, prev_end = sorted_intervals[0][0], sorted_intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            start = sorted_intervals[i][0]
            end = sorted_intervals[i][1]

            if start < prev_end: #overlap
                res += 1
                end = min(prev_end, end)
            prev_end = end
        return res



        