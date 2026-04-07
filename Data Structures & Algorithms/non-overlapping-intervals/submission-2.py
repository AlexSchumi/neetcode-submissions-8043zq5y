class Solution:
    #brute force solution
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        def dfs(i, prev):
            if i == len(intervals):
                return 0
            res = dfs(i + 1, prev)
            if prev == -1 or intervals[prev][1] <= intervals[i][0]:
                res = max(res, 1 + dfs(i + 1, i))
            return res

        return len(intervals) - dfs(0, -1)
    
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        if n == 1:
            return 0

        cur_end = intervals[0][1]
        cnt = 0
        # at least having two
        for i in range(1, n):
            # check if next has overlaps
            if intervals[i][0] < cur_end:
                cnt += 1
                #cur_interval = intervals[i]
                cur_end = min(cur_end, intervals[i][1])
            else:
                cur_end = intervals[i][1]

        return cnt


        

        