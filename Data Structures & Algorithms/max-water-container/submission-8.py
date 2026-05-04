class Solution:
    # for brutal force solution
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                cur = (j - i) * min(heights[i], heights[j])
                res = max(cur, res)

        return res



        