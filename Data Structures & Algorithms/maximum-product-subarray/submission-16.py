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


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp = curMax * num
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            res = max(res, curMax)
        return res


        