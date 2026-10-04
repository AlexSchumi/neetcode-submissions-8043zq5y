class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            water = min(heights[l], heights[r]) * (r - l)
            if water > res:
                res = water
            
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return res
        