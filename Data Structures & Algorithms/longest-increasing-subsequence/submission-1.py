class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [(1, nums[0]) for _ in len(nums)]

        for i in range(1, len(nums)):
            pre_res, pre_max = dp[i-1][0], dp[i-1][1]

            if nums[i] > pre_max: # if it is greater
                cur_res = pre_res + 1
                cur_max = max(nums[i], pre_max)
            else:
                cur_res = 1
                cur_max = nums[i]
            dp[i] = (cur_res, cur_max)
        return dp[-1][0]


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]: # if nums[i] is greater
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)