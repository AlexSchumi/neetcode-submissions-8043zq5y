class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        res = 1
        for i in range(len(nums)):
            num = nums[i]
            cur_res = 1
            while num + 1 in nums:
                num = num + 1
                cur_res += 1
            res = max(cur_res, res)
        return res
                



        