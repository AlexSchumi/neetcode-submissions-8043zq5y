class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            overlap = False
            start_i = intervals[i][0]
            end_i = intervals[i][1]
            # check if overlapping
            while start_i < newInterval[0] < end_i or start_i < newInterval[1] < end_i and i < len(intervals): # means overlap
                start_i = intervals[i][0]
                end_i = intervals[i][1]
                newInterval = [min(start_i, newInterval[0]), max(end_i,  newInterval[1])]
                i += 1
                overlap = True
            if overlap:
                res.append(newInterval)
            else:
                if i < len(intervals):
                    res.append(intervals[i])
        return res


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        # 1. Add all intervals that end before the newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # 2. Merge all overlapping intervals
        # Overlap exists if the current interval starts before or at the newInterval's end
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval) # Add the merged (or single) newInterval

        # 3. Add the rest of the intervals
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
            



        