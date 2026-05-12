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

        