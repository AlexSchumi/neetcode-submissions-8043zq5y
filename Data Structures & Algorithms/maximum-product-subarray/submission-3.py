class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -float('inf')
        for i in range(len(nums)):
            cur_value = nums[i]
            if cur_value > res:
                res = cur_value
            for j in range(i+1, len(nums)):
                cur_value = cur_value * nums[j]

                if cur_value > res:
                    res = cur_value
        return res
            
        