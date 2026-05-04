# brutal force solution
# runtime complexity: O(N^2)
# space complexity: O(1)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                cur = (j - i) * min(heights[i], heights[j])
                res = max(cur, res)

        return res


# optimized solution
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        res = 0
        while i < j:
            cur = (j - i) * min(heights[i], heights[j])
            res = max(cur, res) 

            if heights[i] < heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return res



