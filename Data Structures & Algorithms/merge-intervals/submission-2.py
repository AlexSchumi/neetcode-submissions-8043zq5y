class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        results = []

        for interval in sorted_intervals:
            if not results or results[-1][1] < interval[0]:
                results.append(interval)
            else:
                results[-1][1] = max(results[-1][1], interval[1])
        return results
