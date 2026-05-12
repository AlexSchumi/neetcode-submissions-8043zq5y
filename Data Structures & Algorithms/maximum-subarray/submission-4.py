# brute-force solution
# runtime: O(N^2)
# space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(len(nums)):
            cur_sum = nums[i]
            res = max(cur_sum, res)

            for j in range(i+1, len(nums)):
                cur_sum += nums[j]
                res = max(cur_sum, res)
        return res


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub




        