# brute force solution
# runtime: O(N^2)
# space: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = float('-inf')
        for i in range(len(nums)):
            res = 1
            for j in range(i, len(nums)):
                res = res * nums[j]
                result = max(res, result)
        return result

        